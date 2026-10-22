# logging.handlers: `logging.handlers.QueueHandler`

### QueueHandler

Added in version 3.2.

Living in the `logging.handlers` module, the `QueueHandler` class lets you deliver logging messages onto a queue — for instance the kind built in the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) or [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) modules.

Paired with the `QueueListener` class, `QueueHandler` makes it possible for handlers to run their work on a thread apart from the one doing the logging. That matters in web applications, and in other service applications too, where client-serving threads must answer as fast as they can while slower jobs (say, emailing through `SMTPHandler`) run off on a separate thread.

 *class *logging.handlers.QueueHandler(*queue*)

Hands back a fresh instance of the `QueueHandler` class. Its setup takes the queue that messages will be sent to. The *queue* may be any queue-like object; the `enqueue()` method takes it as-is and has to know how to put messages onto it. The queue is not *required* to carry the task tracking API, so you are free to use [`SimpleQueue`](https://docs.python.org/3.14/library/queue.html#queue.SimpleQueue) instances for *queue*.

Note

When you work with [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing), steer clear of [`SimpleQueue`](https://docs.python.org/3.14/library/queue.html#queue.SimpleQueue) and reach for [`multiprocessing.Queue`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue) instead.

Warning

The [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module keeps an internal logger that is created and reached via [`get_logger()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.get_logger). [`multiprocessing.Queue`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue) logs `DEBUG` level messages whenever items are placed on it. Should those log messages then be handled by a `QueueHandler` using that very same `multiprocessing.Queue` instance, a deadlock or unbounded recursion results.

[Subject index](INDEX.md) · [Previous](http-handler-record-mapping-and-emission.md) · [Continue](queue-handler-emission-and-enqueue.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
