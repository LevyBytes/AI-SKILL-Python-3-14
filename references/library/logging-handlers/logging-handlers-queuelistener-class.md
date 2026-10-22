# logging.handlers: `logging.handlers.QueueListener`

### QueueListener

Added in version 3.2.

Living in the `logging.handlers` module, the `QueueListener` class lets you take in logging messages off a queue — for instance the kind built in the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) or [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) modules. An internal thread pulls the messages from a queue and, on that same thread, forwards them to one or more handlers for processing. Although `QueueListener` is not a handler itself, it appears here because it operates in close partnership with `QueueHandler`.

Paired with the `QueueHandler` class, `QueueListener` makes it possible for handlers to run their work on a thread apart from the one doing the logging. That matters in web applications, and in other service applications too, where client-serving threads must answer as fast as they can while slower jobs (say, emailing through `SMTPHandler`) run off on a separate thread.

 *class *logging.handlers.QueueListener(*queue*, **handlers*, *respect_handler_level=False*)

Hands back a fresh instance of the `QueueListener` class. Its setup takes the queue that messages will be sent to plus a list of handlers that will process the entries placed on the queue. The queue may be any queue-like object; it is forwarded as-is to the `dequeue()` method, which has to know how to pull messages off it. The queue is not *required* to carry the task tracking API (though it is used where available), so you are free to use [`SimpleQueue`](https://docs.python.org/3.14/library/queue.html#queue.SimpleQueue) instances for *queue*.

Note

When you work with [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing), steer clear of [`SimpleQueue`](https://docs.python.org/3.14/library/queue.html#queue.SimpleQueue) and reach for [`multiprocessing.Queue`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue) instead.

With `respect_handler_level` set to `True`, a handler's level is honored (weighed against the message's level) when judging whether to forward messages to that handler; otherwise the behaviour matches earlier Python versions — every message goes to every handler unconditionally.

Changed in version 3.5: The `respect_handler_level` argument was added.

Changed in version 3.14: `QueueListener` may now serve as a context manager through [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with). Entering the context starts the listener; leaving it stops the listener. [`__enter__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__enter__) returns the `QueueListener` object.

[Subject index](INDEX.md) · [Previous](queue-handler-emission-and-enqueue.md) · [Continue](queue-listener-dequeue-and-sentinel.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
