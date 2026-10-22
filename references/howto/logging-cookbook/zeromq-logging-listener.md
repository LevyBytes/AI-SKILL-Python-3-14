# ZeroMQ logging listener

### Subclass `QueueListener`

Subclassing [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) is likewise an option for pulling messages from other sorts of queues, a ZeroMQ ‘subscribe’ socket for instance. Here is one example:

```python
import logging
from logging.handlers import QueueListener
import zmq

class ZeroMQSocketListener(QueueListener):
    def __init__(self, uri, /, *handlers, **kwargs):
        self.ctx = kwargs.get('ctx') or zmq.Context()
        socket = zmq.Socket(self.ctx, zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, '')  # subscribe to everything
        socket.connect(uri)
        super().__init__(socket, *handlers, **kwargs)

    def dequeue(self, block):
        msg = self.queue.recv_json(flags=0 if block else zmq.NOBLOCK)
        return logging.makeLogRecord(msg)

```

Use the [ZeroMQ handler](zeromq-logging-handler.md) as the publisher. Install the optional pyzmq dependency for this example.

[Subject index](INDEX.md).
