#!/usr/bin/env python3

import slixmpp

from slixmpp.xmlstream import tostring
from slixmpp.exceptions import IqError
from xml.etree.ElementTree import fromstring
from xml.sax.saxutils import escape
import asyncio
from .utils import format_iso_date
from .errors import NotAuthorized, ServiceUnavailable
from .data import Data


class ClientAsync:
    def __init__(self, xmpp_client, proxy_full_jid):
        self.xmpp_client = xmpp_client
        self.proxy_full_jid = proxy_full_jid

    # Identifier: urn:dev:prm:30001610071843_consumption/active_power/raw
    async def get_records(self, identifier, start_date=None, end_date=None):
        iq = self.xmpp_client.Iq()
        iq["type"] = "set"
        iq["to"] = self.proxy_full_jid

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
              node="get_records"
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
            else:
                raise e

        command = response.xml.find(".//{http://jabber.org/protocol/commands}command")
        if command.attrib["status"] == "completed":
            data = command.find(".//{urn:quoalise:0}quoalise")
            return Data(data)
        else:
            raise RuntimeError("Unexpected iq response: " + tostring(response.xml))

    @classmethod
    async def connect(cls, client_jid, client_password, server_full_jid):
        xmpp_client = slixmpp.ClientXMPP(client_jid, client_password)
        xmpp_client.connect()

        session_stard_event = asyncio.Future()

        def handler(event_data):
            if not session_stard_event.done():
                session_stard_event.set_result(event_data)

        xmpp_client.add_event_handler(
            "session_start",
            handler,
            disposable=True,
        )

        await asyncio.wait_for(session_stard_event, 30)
        return cls(xmpp_client, server_full_jid)

    def disconnect(self):
        self.xmpp_client.disconnect()
        # Avoids « Task was destroyed but it is pending! » when closing the event loop,
        # might not be needed in future versions
        self.xmpp_client._run_out_filters.cancel()


class Client:
    def __init__(self, client_async, event_loop):
        self.client_async = client_async
        self.loop = event_loop

    @classmethod
    def connect(cls, client_jid, client_password, server_full_jid, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()
        client_async = loop.run_until_complete(
            ClientAsync.connect(client_jid, client_password, server_full_jid)
        )
        return cls(client_async, loop)

    def get_records(self, identifier, start_date=None, end_date=None):
        return self.loop.run_until_complete(
            self.client_async.get_records(identifier, start_date, end_date)
        )

    def disconnect(self):
        self.client_async.disconnect()
