# Sending and receiving logging events across a network

### Sending and receiving logging events across a network

Imagine you want to ship logging events over a network and process them once they arrive. One easy approach is to bolt a [`SocketHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler) instance onto the root logger on the sending side:

```python
import logging, logging.handlers

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SocketHandler('localhost',
                    logging.handlers.DEFAULT_TCP_LOGGING_PORT)
# don't bother with a formatter, since a socket handler sends the event as
# an unformatted pickle
rootLogger.addHandler(socketHandler)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

```

On the receiving side, you can stand up a receiver built on the [`socketserver`](https://docs.python.org/3.14/library/socketserver.html#module-socketserver) module. Here is a minimal functioning example:

[Subject index](INDEX.md) · [Following source continuation](complete-socket-logging-receiver-implementation.md) · [Previous source context](dealing-with-handlers-that-block.md)
