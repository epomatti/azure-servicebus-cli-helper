from config import get_connection_string
from azure.servicebus import ServiceBusClient


def get_servicebus_client():
    connection_string = get_connection_string()
    return ServiceBusClient.from_connection_string(connection_string)


def purge(queue_name):
    with get_servicebus_client() as servicebus_client:
        # get the Queue Receiver object for the queue
        receiver = servicebus_client.get_queue_receiver(
            queue_name=queue_name, max_wait_time=5
        )
        with receiver:
            for msg in receiver:
                print("Received: " + str(msg))
                # complete the message so that the message is removed from the queue
                receiver.complete_message(msg)