# Dealing with handlers that block

### Dealing with handlers that block

There are times when your logging handlers must complete their work without holding up the thread doing the logging. Web applications hit this frequently, though it crops up elsewhere too.

One frequent offender that exhibits laggy behaviour is the [`SMTPHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SMTPHandler): dispatching email can drag on, for assorted reasons beyond the developer's reach (say, an underperforming mail server or shaky network). Yet virtually any handler built on the network may stall: even a [`SocketHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler) call could trigger a DNS lookup behind the scenes that runs too slowly (and that lookup may sit deep within the socket library code, beneath the Python layer, beyond your reach).

A workable fix is a two-stage design. In the first stage, hook up just a [`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler) to the loggers reached from performance-critical threads. Those simply deposit into their queue, which you can size with ample capacity or set up with no ceiling on how large it grows. Pushing onto the queue is usually accepted swiftly, although you will probably want to guard against the [`queue.Full`](https://docs.python.org/3.14/library/queue.html#queue.Full) exception in your code just to be safe. If you write libraries that contain performance-critical threads, make sure to note this (along with advice to attach only `QueueHandlers` to your loggers) so the developers consuming your code are aware.

The second stage of the fix is [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener), crafted to complement [`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler). A `QueueListener` is quite straightforward: you hand it a queue plus some handlers, and it spins up an internal thread that watches the queue for LogRecords arriving from `QueueHandlers` (or indeed any other origin of `LogRecords`). Those `LogRecords` get pulled off the queue and forwarded to the handlers to be processed.

What you gain from keeping [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) as its own class is that a single instance can serve several `QueueHandlers`. That is friendlier on resources than, for instance, maintaining threaded variants of every existing handler class, each of which would burn one thread per handler with nothing much gained.

Here is a sample that puts both classes to work (imports left out):

```python
que = queue.Queue(-1)  # no limit on size
queue_handler = QueueHandler(que)
handler = logging.StreamHandler()
listener = QueueListener(que, handler)
root = logging.getLogger()
root.addHandler(queue_handler)
formatter = logging.Formatter('%(threadName)s: %(message)s')
handler.setFormatter(formatter)
listener.start()
# The log output will display the thread which generated
# the event (the main thread) rather than the internal
# thread which monitors the internal queue. This is what
# you want to happen.
root.warning('Look out!')
listener.stop()

```

which, on being run, yields:

```none
MainThread: Look out!

```

Note

While the preceding discussion centred on slow logging handlers rather than async code as such, it is worth flagging that when you log from async code, network and even file handlers may cause trouble (stalling the event loop), because certain logging happens within [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) internals. Wherever an application makes use of async code, it is probably wise to adopt the approach above for logging, so that any blocking code executes only inside the `QueueListener` thread.

Changed in version 3.5: Before Python 3.5, the [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) handed every message pulled from the queue to every handler supplied at construction. (The reasoning was that all level filtering happened on the opposite side, where the queue gets populated.) Starting with 3.5, you can alter that behaviour by handing the listener's constructor the keyword argument `respect_handler_level=True`. With that set, the listener weighs each message's level against the handler's level and forwards a message to a handler only when doing so is appropriate.

Changed in version 3.14: The [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) supports being started (and stopped) through the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. As an illustration:

```python
with QueueListener(que, handler) as listener:
    # The queue listener automatically starts
    # when the 'with' block is entered.
    pass
# The queue listener automatically stops once
# the 'with' block is exited.

```

[Subject index](INDEX.md) · [Previous source context](configuration-server-example.md) · [Following source context](sending-and-receiving-logging-events-across-a-network.md)
