# logging / Handler Objects: `createLock()`, `acquire()`, `release()`, `setLevel()`, `setFormatter()`, `addFilter()`, `removeFilter()`, `filter()`, `flush()`, `close()`, `handle()`, `handleError()`, `format()`, `emit()`

createLock()

Initializes a thread lock usable for serializing access to underlying I/O functionality that may not be threadsafe.

 acquire()

Acquires the thread lock created with `createLock()`.

 release()

Releases the thread lock acquired with `acquire()`.

 setLevel(*level*)

Sets this handler's threshold to *level*. Logging messages less severe than *level* will be disregarded. At the moment a handler is created, its level is set to `NOTSET` (which leads to every message being processed).

See Logging Levels for a list of levels.

Changed in version 3.2: As an alternative to the integer constants such as `INFO`, the *level* parameter now also takes a string spelling of the level such as ‘INFO’.

 setFormatter(*fmt*)

Sets this handler's formatter to *fmt*. The *fmt* argument has to be a `Formatter` instance or `None`.

 addFilter(*filter*)

Adds the specified filter *filter* to this handler.

 removeFilter(*filter*)

Removes the specified filter *filter* from this handler.

 filter(*record*)

Run this handler's filters against the record and hand back `True` when the record is to be processed. The filters are consulted one after another, until one of them yields a false value. When none yield a false value, the record will be emitted. When one yields a false value, the handler won't emit the record.

 flush()

Ensure every bit of logging output has been flushed. This version is a no-op and is intended for subclasses to implement.

 close()

Tidy up any resources the handler used. This version produces no output but pulls the handler out of an internal map of handlers, which serves handler lookup by name.

Subclasses should make sure this gets called from overridden `close()` methods.

 handle(*record*)

Conditionally emits the given logging record, subject to whatever filters were added to the handler. The record's actual emission is wrapped by acquiring then releasing the I/O thread lock.

 handleError(*record*)

Handlers should call this method whenever an exception crops up during an `emit()` call. When the module-level attribute `raiseExceptions` is `False`, exceptions are silently swallowed. That's mostly what's wanted in a logging system — the majority of users won't care about errors inside the logging system, being more concerned with application errors. You could, however, swap in a custom handler should you wish. The given record is the one that was under processing when the exception arose. (The default value of `raiseExceptions` is `True`, since that proves more useful during development).

 format(*record*)

Do formatting for a record: when a formatter is set, use it. If not, fall back on the module's default formatter.

 emit(*record*)

Do whatever is necessary to actually log the given logging record. This version is meant to be implemented by subclasses and so raises a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Warning

This method runs after a handler-level lock is acquired, which is released once this method returns. While overriding this method, bear in mind that you should be wary of calling anything that reaches into other parts of the logging API which might do locking, since that could end in a deadlock. To be precise:

- Logging configuration APIs acquire the module-level lock, and afterwards individual handler-level locks as those handlers get configured.

- Plenty of logging APIs lock the module-level lock. Should such an API be called from this method, it could trigger a deadlock if a configuration call happens on another thread, because that other thread will reach for the module-level lock *before* the handler-level lock, while this thread reaches for the module-level lock *after* the handler-level lock (since within this method, the handler-level lock has already been acquired).

For a list of handlers included as standard, see [`logging.handlers`](https://docs.python.org/3.14/library/logging.handlers.html#module-logging.handlers).

[Subject index](INDEX.md) · [Previous](logging-handler-class-to-init.md) · [Continue](logging-formatter-class.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.Handler; __init__](logging-handler-class-to-init.md) · [Owning module, declaration or section: Handler Objects](logging-handler-class-to-init.md)
