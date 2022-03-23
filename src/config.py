from configparser import ConfigParser

def get_config():
    parser = ConfigParser()
    parser.read('config.ini')
    return parser

def get_connection_string():
    parser = get_config()
    connection_string = parser.get('AZURE', 'SERVICE_BUS_CONNECTION_STRING')
    # TODO: validate before return
    return connection_string
