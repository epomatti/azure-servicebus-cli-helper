from config import get_connection_string
from configparser import ConfigParser
from azure.servicebus import QueueClient, Message, ServiceBusClient

def get_queue_client(queue_name):
    connection_string = get_connection_string()
    return QueueClient.from_connection_string(
        connection_string, queue_name)

def get_servicebus_client():
    connection_string = get_connection_string()
    return ServiceBusClient.from_connection_string(
        connection_string)

def purge(queue_name):    
    queue_client = get_queue_client(queue_name)
    with queue_client.get_receiver() as queue_receiver:
        messages = queue_receiver.fetch_next(timeout=3)
        for message in messages:
            print(message)
            message.complete()

def list_queues():
    client = get_servicebus_client()
    queues = client.list_queues()
    for q in queues:
        print(q.name)