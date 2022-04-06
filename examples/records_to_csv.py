#!/usr/bin/env python3

import os
import sys
import argparse
import csv
import datetime as dt

import quoalise

# import logging
# logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(
    description="Get records from previous week in a csv file"
)

parser.add_argument(
    "server_jid",
    help="full jid of the server providing the API, "
    + "i.e., sge-proxy@provider.tld/proxy",
)
parser.add_argument(
    "data_id", help="data identifier, i.e., urn:dev:ow:10e2073a0108006_voltage"
)

args = parser.parse_args()

quoalise_user = os.environ.get("QUOALISE_USER")
quoalise_password = os.environ.get("QUOALISE_PASSWORD")
if quoalise_user is None or quoalise_password is None:
    sys.exit(
        "Client credentials not found in environment variables:\n"
        + "QUOALISE_USER should be set to your xmpp bare jid\n"
        + "QUOALISE_PASSWORD should be set to your xmpp password"
    )

end_date = dt.date.today() - dt.timedelta(days=1)
start_date = end_date - dt.timedelta(days=6)

client = quoalise.Client.connect(quoalise_user, quoalise_password)
data = client.get_records(args.server_jid, args.data_id, start_date, end_date)

writer = csv.writer(sys.stdout)

for record in data.records:
    writer.writerow([record.time.isoformat(), record.value])
