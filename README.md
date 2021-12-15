# quoalise

## Development

Quoalise is not yet available on PyPI. You can install the package in "editable" mode.

```bash
pip install -r dev-requirements.txt
pip install -e .
```

## Command line usage

```bash
quoalise get-records --help
```

```bash
export QUOALISE_USER="you@xmppx.io"
export QUOALISE_PASSWORD="************"
```

```bash
quoalise get-records --server user@xmpp-server.tld --from 2021-01-01 --to 2021-01-07 urn:dev:prm:30001610071843_consumption/active_power/raw
```

## Contributing

Please run black and flake8 before commit. It can be done automatically with a git pre-commit hook:

```bash
pre-commit install
```