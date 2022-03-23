# Azure Service Bus Purge

### Running it

Install the dependencies:

```sh
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Setup the `config.ini` file:

```sh
# add the service bus connection string to this file
cp config_example.ini config.ini
```

Purge:

```sh
# purge
python3 src/main.py purge 'queue_name'
```

### Purple Explorer

Checkout this project for an open source cross-platform experience:

https://github.com/telstrapurple/PurpleExplorer