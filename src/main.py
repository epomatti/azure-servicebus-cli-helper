from servicebus import purge, list_queues
import sys

command = sys.argv[1]

if command == 'purge':
    queue = sys.argv[2]
    purge(queue)
elif command == 'list_queues':
    list_queues()
else:
    print('Invalid command: ', command)