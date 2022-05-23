#!/usr/bin/env python3

from typing import Any, AsyncGenerator, Coroutine, Iterator, Tuple, Optional
import datetime as dt
from xmlrpc.client import boolean

import slixmpp
from slixmpp.xmlstream import tostring
from slixmpp.exceptions import IqError
from slixmpp.xmlstream.matcher import MatchXPath
from slixmpp.xmlstream.handler import CoroutineCallback
from xml.etree.ElementTree import fromstring
from xml.sax.saxutils import escape
import asyncio
from .utils import format_iso_date
from .errors import NotAuthorized, ServiceUnavailable, ConnectionFailed, BadRequest
from .data import Data


class ClientAsync:
    def __init__(self, xmpp_client: slixmpp.ClientXMPP):
        self.xmpp_client = xmpp_client
        self.incoming_data: asyncio.Queue[Data] = asyncio.Queue()

    async def get_history(
        self,
        proxy_full_jid: str,
        identifier: str,
        start_date: Optional[dt.date] = None,
        end_date: Optional[dt.date] = None,
    ) -> Data:
        iq = self.xmpp_client.Iq()
        iq["type"] = "set"
        iq["to"] = proxy_full_jid

        # TODO(cyril) use a proper element builder

        if start_date is not None:
            start_date_field = f"""
                <field var="start_date" type="text-single">
                  <value>{escape(format_iso_date(start_date))}</value>
                </field>
            """
        else:
            start_date_field = ""

        if end_date is not None:
            end_date_field = f"""
                <field var="end_date" type="text-single">
                  <value>{escape(format_iso_date(end_date))}</value>
                </field>
            """
        else:
            end_date_field = ""

        iq.append(
            fromstring(
                f"""
            <command
              xmlns="http://jabber.org/protocol/commands"
              node="get_history"
              action="execute">
              <x xmlns="jabber:x:data" type="submit">
                <field var="identifier" type="text-single">
                  <value>{escape(identifier)}</value>
                </field>
                {start_date_field}
                {end_date_field}
              </x>
            </command>
        """
            )
        )

        try:
            response = await iq.send()
        except IqError as e:
            if e.condition == "not-authorized":
                raise NotAuthorized(e.text)
            elif e.condition == "service-unavailable":
                raise ServiceUnavailable(e.text)
            elif e.condition == "bad-request":
                raise BadRequest(e.text)
            else:
                raise e

        command = response.xml.find(".//{http://jabber.org/protocol/commands}command")
        if command.attrib["status"] == "completed":
            data = command.find(".//{urn:quoalise:0}quoalise/{urn:quoalise:0}data")
            return Data.from_xml(data)
        else:
            raise RuntimeError("Unexpected iq response: " + tostring(response.xml))

    @classmethod
    async def connect(
        cls,
        client_jid: str,
        client_password: str,
        address: Optional[Tuple[str, str]] = None,
        priority: int = -1,
    ) -> "ClientAsync":
        """
        priority:
          Negative prevents to receive messages that are not explicitely
          addressed to this resource. Use a positive value when waiting for
          subscription records, use a negative value when polling records.
        """
        xmpp_client = slixmpp.ClientXMPP(client_jid, client_password)
        xmpp_client.connect(address=address)

        session_state: asyncio.Future[boolean] = asyncio.Future()
        error = None

        def session_start_waiter(event_data: Any) -> None:
            if not session_state.done():
                session_state.set_result(True)

        def session_end_handler(event_data: Any) -> None:
            if not session_state.done():
                nonlocal error
                error = ConnectionFailed("XMPP server ended the session")
                session_state.set_result(False)

        def connection_failed_handler(event_data: Any) -> None:
            if not session_state.done():
                nonlocal error
                error = ConnectionFailed(f"XMPP server is not reachable, {event_data}")
                session_state.set_result(False)

        def failed_auth_handler(event_data: Any) -> None:
            if not session_state.done():
                nonlocal error
                error = ConnectionFailed("Invalid username or password")
                session_state.set_result(False)

        xmpp_client.add_event_handler(
            "session_start",
            session_start_waiter,
            disposable=True,
        )

        xmpp_client.add_event_handler(
            "session_end",
            session_end_handler,
            disposable=True,
        )

        xmpp_client.add_event_handler(
            "connection_failed",
            connection_failed_handler,
            disposable=True,
        )

        xmpp_client.add_event_handler(
            "failed_auth",
            failed_auth_handler,
            disposable=True,
        )

        await asyncio.wait_for(session_state, 10)

        if error:
            raise error

        client = cls(xmpp_client)

        xmpp_client.register_handler(
            CoroutineCallback(
                "Quoalise Data",
                MatchXPath(
                    "{jabber:client}message/"
                    + "{urn:quoalise:0}quoalise/{urn:quoalise:0}data"
                ),
                client.handle_message_data,
            )
        )

        xmpp_client.send_presence(ppriority=priority)

        return client

    def disconnect(self) -> None:
        self.xmpp_client.disconnect()
        # Avoids « Task was destroyed but it is pending! » when closing the event loop,
        # might not be needed in future versions
        # self.xmpp_client._run_out_filters.cancel()

    async def handle_message_data(self, message: slixmpp.Message) -> None:
        data = message.xml.find("{urn:quoalise:0}quoalise/{urn:quoalise:0}data")
        data = Data.from_xml(data)
        self.incoming_data.put_nowait(data)

    async def wait_for_data(self) -> Data:
        return await self.incoming_data.get()

    async def listen(self) -> AsyncGenerator[Coroutine[Any, Any, Data], None]:
        while True:
            yield self.wait_for_data()


class Client:
    def __init__(
        self, client_async: ClientAsync, event_loop: asyncio.AbstractEventLoop
    ):
        self.client_async = client_async
        self.loop = event_loop

    @classmethod
    def connect(
        cls,
        client_jid: str,
        client_password: str,
        priority: int = -1,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        address: Optional[Tuple[str, str]] = None,
    ) -> "Client":
        if loop is None:
            loop = asyncio.get_event_loop()
        client_async = loop.run_until_complete(
            ClientAsync.connect(
                client_jid, client_password, address=address, priority=priority
            )
        )
        return cls(client_async, loop)

    def get_history(
        self,
        proxy_full_jid: str,
        identifier: str,
        start_date: Optional[dt.date] = None,
        end_date: Optional[dt.date] = None,
    ) -> Data:
        return self.loop.run_until_complete(
            self.client_async.get_history(
                proxy_full_jid, identifier, start_date, end_date
            )
        )

    def listen(self) -> Iterator[Data]:
        while True:
            yield self.loop.run_until_complete(self.client_async.wait_for_data())

    def disconnect(self) -> None:
        self.client_async.disconnect()
