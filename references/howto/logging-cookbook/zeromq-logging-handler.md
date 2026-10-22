# ZeroMQ logging handler

### Subclassing QueueHandler and QueueListener- a ZeroMQ example

### Subclass `QueueHandler`

A [`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler) subclass lets you route messages to other sorts of queues, a ZeroMQ ‘publish’ socket among them. In the example that follows, the socket is built on its own and handed to the handler (serving as its ‘queue’):

```python
from logging.handlers import QueueHandler
import zmq   # using pyzmq, the Python binding for ZeroMQ
import json  # for serializing records portably

ctx = zmq.Context()
sock = zmq.Socket(ctx, zmq.PUB)  # or zmq.PUSH, or other suitable value
sock.bind('tcp://*:5556')        # or wherever

class ZeroMQSocketHandler(QueueHandler):
    def enqueue(self, record):
        self.queue.send_json(record.__dict__)

handler = ZeroMQSocketHandler(sock)

```

Naturally other arrangements exist, such as supplying the handler with the data it needs to build the socket:

```python
class ZeroMQSocketHandler(QueueHandler):
    def __init__(self, uri, socktype=zmq.PUB, ctx=None):
        self.ctx = ctx or zmq.Context()
        socket = zmq.Socket(self.ctx, socktype)
        socket.bind(uri)
        super().__init__(socket)

    def enqueue(self, record):
        self.queue.send_json(record.__dict__)

    def close(self):
        self.queue.close()

```

The second handler definition is an alternative using the imports above. Install the optional pyzmq dependency. Pair it with the [ZeroMQ listener](zeromq-logging-listener.md).

[Subject index](INDEX.md).
