# Azure Service Bus CLI Helper

A cross-platform CLI helper to run commands on Azure Service Bus.

## Why

Microsoft does not provide an official management client and [Service Bus Explorer](https://github.com/paolosalvatori/ServiceBusExplorer) is exclusive for Windows.

## Usage

**Caution:** Confirm messages are not yet implemented.

Count messages in a queue:

```s
python3 src/main.py count queue_name
```

Purge messages in a queue:

```s
python3 src/main.py purge queue_name
```

## Running it

Install dependencies:

```s
apt-get install python3-venv
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Create `config.ini` file with the connection string information.