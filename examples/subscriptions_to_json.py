#!/usr/bin/env python3

import os
import sys

import quoalise

# import logging
# logging.basicConfig(level=logging.DEBUG)

quoalise_user = os.environ.get("QUOALISE_USER")
quoalise_password = os.environ.get("QUOALISE_PASSWORD")
if quoalise_user is None or quoalise_password is None:
    sys.exit(
        "Client credentials not found in environment variables:\n"
        + "QUOALISE_USER should be set to your xmpp bare jid\n"
        + "QUOALISE_PASSWORD should be set to your xmpp password"
    )

# Ensure priority is positive, allowwing XMPP client to receive messages
# sent to quoalise_user bare jid.
client = quoalise.Client.connect(quoalise_user, quoalise_password, priority=1)

for data in client.listen():
    print(data.to_json(indent=2))
