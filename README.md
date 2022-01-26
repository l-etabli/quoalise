# quoalise

## Install

### Using your distribution python package

Install dependencies:

```
sudo apt install python3-slixmpp
```

The `quoalise` command can be run from the Python module:

```
git clone https://github.com/consometers/quoalise.git
cd quoalise/src
python3 -m quoalise <arguments>
```

### In a Python virtual environment

Alternatively, you can install the `quoalise` command in virtual environment. Quoalise is not yet available on PyPI, install the package in "editable" mode:

```bash
git clone https://github.com/consometers/quoalise.git
cd quoalise
python3 -m venv env
source env/bin/activate
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
quoalise get-records user@xmpp-server.tld/resource urn:dev:prm:30001610071843_consumption/active_power/raw --start-date 2021-12-01 --end-date 2021-12-05
```

## Contributing

Please run black and flake8 before commit. It can be done automatically with a git pre-commit hook:

```bash
pre-commit install
```