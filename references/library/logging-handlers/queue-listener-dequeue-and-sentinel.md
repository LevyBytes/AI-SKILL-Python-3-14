# logging.handlers.QueueListener: `dequeue()`, `prepare()`, `handle()`, `start()`, `stop()`, `enqueue_sentinel()`

dequeue(*block*)

Pulls a record off and returns it, blocking if you ask it to.

The base implementation leans on `get()`. Override this method when you would like to use timeouts or work against queue implementations of your own.

 prepare(*record*)

Ready a record for handling.

This implementation merely hands back the record it was given. Override it when you need any custom marshalling or reshaping of the record ahead of passing it to the handlers.

 handle(*record*)

Handle a record.

This simply walks the handlers, offering each the record to handle. The object actually passed to the handlers is whatever `prepare()` returned.

 start()

Start the listener.

Doing so spins up a background thread that watches the queue for LogRecords awaiting processing.

Changed in version 3.14: Raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) when invoked while the listener is already running.

 stop()

Stop the listener.

This signals the thread to wind down and then waits until it has. Bear in mind that skipping this call before your application exits can leave some records lingering on the queue, never to be processed.

 enqueue_sentinel()

Puts a sentinel on the queue to signal the listener to quit. This implementation leans on `put_nowait()`. Override this method when you would like to use timeouts or work against queue implementations of your own.

Added in version 3.3.

See also

Module [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging)

API reference covering the logging module.

Module [`logging.config`](https://docs.python.org/3.14/library/logging.config.html#module-logging.config)

Configuration API covering the logging module.

[Subject index](INDEX.md) · [Previous](logging-handlers-queuelistener-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.QueueListener](logging-handlers-queuelistener-class.md) · [Owning module, declaration or section: QueueListener](logging-handlers-queuelistener-class.md)
