import sys
import os
import argparse
import logging
from typing import Iterable
from xml.dom import minidom
import xml.etree.ElementTree as ET

from .client import Client
from .utils import parse_iso_date
from .errors import NotAuthorized, ServiceUnavailable, ConnectionFailed
from .data import Data


def cli() -> int:

    parser = argparse.ArgumentParser(description="Access a Quoalise API.")

    parser.add_argument("--debug", action="store_true", help="Show xmpp debug logs")

    parser.add_argument(
        "--format",
        choices={"quoalise", "json", "csv"},
        default="json",
        help="default: %(default)s",
    )

    subparsers = parser.add_subparsers(help="command", dest="command")

    parser_client = subparsers.add_parser("get-records", help="Get records")
    parser_client.add_argument(
        "server_jid",
        help="full jid of the server providing the API, "
        + "i.e., sge-proxy@provider.tld/proxy",
    )
    parser_client.add_argument(
        "data_id", help="data identifier, i.e., urn:dev:ow:10e2073a0108006_voltage"
    )
    parser_client.add_argument("--start-date", metavar="YYYY-MM-DD")
    parser_client.add_argument("--end-date", metavar="YYYY-MM-DD")

    subparsers.add_parser("listen", help="Listen for incoming messages")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    quoalise_user = os.environ.get("QUOALISE_USER")
    quoalise_password = os.environ.get("QUOALISE_PASSWORD")
    if quoalise_user is None or quoalise_password is None:
        sys.exit(
            "Client credentials not found in environment variables:\n"
            + "QUOALISE_USER should be set to your xmpp bare jid\n"
            + "QUOALISE_PASSWORD should be set to your xmpp password"
        )

    # Negative priority prevents to receive messages that are not explicitely
    # addressed to this resource. Use a positive value when waiting for
    # subscription records, use a negative value when polling records.
    if args.command == "get-records":
        priority = -1
    else:
        priority = 1

    client = Client.connect(quoalise_user, quoalise_password, priority=priority)

    try:
        if args.command == "get-records":
            if args.start_date is not None:
                args.start_date = parse_iso_date(args.start_date)

            if args.end_date is not None:
                args.end_date = parse_iso_date(args.end_date)

            data_stream: Iterable[Data] = [
                client.get_records(
                    args.server_jid, args.data_id, args.start_date, args.end_date
                )
            ]
        elif args.command == "listen":
            data_stream = client.listen()
        else:
            raise ValueError(f"Unexpected command {args.command}")

        for data in data_stream:
            if args.format == "quoalise":
                print(
                    minidom.parseString(ET.tostring(data.to_xml())).toprettyxml(
                        indent="  "
                    )
                )
            elif args.format == "json":
                print(data.to_json(indent=2))
            else:
                raise ValueError(f"Unexpected format {args.format}")

    except NotAuthorized as e:
        print(f"You are not authorized to access the resource: {e}", file=sys.stderr)

    except ServiceUnavailable as e:
        print(f"{args.server_jid} is not available: {e}", file=sys.stderr)

    except ConnectionFailed as e:
        print(f"XMPP user {quoalise_user} is not able to connect: {e}", file=sys.stderr)

    except Exception as e:
        if args.debug:
            raise e
        else:
            print(str(e), file=sys.stderr)

    return -1


if __name__ == "__main__":
    sys.exit(cli())
