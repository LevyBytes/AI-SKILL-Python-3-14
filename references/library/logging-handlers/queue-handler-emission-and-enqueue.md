# logging.handlers.QueueHandler: `emit()`, `prepare()`, `enqueue()`

emit(*record*)

Places the prepared LogRecord onto the queue. Were an exception to arise (say, a bounded queue having filled up), the [`handleError()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.handleError) method steps in to deal with the error. That can leave the record quietly discarded (when [`logging.raiseExceptions`](https://docs.python.org/3.14/library/logging.html#logging.raiseExceptions) is `False`) or a message emitted to `sys.stderr` (when `logging.raiseExceptions` is `True`).

 prepare(*record*)

Readies a record for queuing. Whatever this method hands back is what gets enqueued.

The base implementation formats the record so that the message, arguments, exception and stack information (where present) merge together. It likewise strips unpickleable items out of the record in place. Concretely, it overwrites the record's `msg` and `message` attributes with the merged message (got by calling the handler's [`format()`](https://docs.python.org/3.14/library/functions.html#format) method), and sets the `args`, `exc_info` and `exc_text` attributes to `None`.

Override this method when you would rather turn the record into a dict or a JSON string, or send a tweaked copy of the record while leaving the original untouched.

Note

The base implementation formats the message together with its arguments, points the `message` and `msg` attributes at that formatted message, and sets the `args` and `exc_text` attributes to `None` so the record can be pickled and so no further formatting is attempted. The upshot is that a handler over on the `QueueListener` side lacks the information for custom formatting — of exceptions, for example. You may want to subclass `QueueHandler` and override this method to, say, keep `exc_text` from being set to `None`. Bear in mind the `message` / `msg` / `args` changes exist to make the record pickleable, and whether you can sidestep them depends on whether your `args` are themselves pickleable. (Bear in mind too that you may have to weigh not only your own code but also the code in whatever libraries you draw on.)

 enqueue(*record*)

Places the record onto the queue by way of `put_nowait()`; override this when you would rather have blocking behaviour, a timeout, or a queue implementation of your own.

 listener

When the handler is built from configuration through [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig), this attribute holds a `QueueListener` instance meant to accompany the handler. Otherwise it is `None`.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](logging-handlers-queuehandler-class.md) · [Continue](logging-handlers-queuelistener-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.QueueHandler](logging-handlers-queuehandler-class.md) · [Owning module, declaration or section: QueueHandler](logging-handlers-queuehandler-class.md)
