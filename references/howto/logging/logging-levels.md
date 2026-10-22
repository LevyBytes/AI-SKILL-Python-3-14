# Logging Levels

### Logging Levels

The table below lists the numeric values of the logging levels. These mainly matter when you intend to define levels of your own and need them to sit at particular values relative to the predefined ones. Defining a level with the same numeric value overwrites the predefined value; the predefined name disappears.

| Level | Numeric value |
| --- | --- |
| `CRITICAL` | 50 |
| `ERROR` | 40 |
| `WARNING` | 30 |
| `INFO` | 20 |
| `DEBUG` | 10 |
| `NOTSET` | 0 |

Loggers can carry levels too, assigned either by the developer or by loading a stored logging configuration. Whenever a logging method runs on a logger, the logger weighs its own level against the level tied to that method call. Should the logger's level exceed the method call's, no logging message is produced at all. That is the fundamental mechanism governing how verbose the logging output is.

Logging messages are represented as instances of the [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) class. Once a logger determines that an event truly should be logged, it constructs a `LogRecord` instance from the logging message.

Logging messages move through a dispatch mechanism by way of *handlers*, which are instances of subclasses of the [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) class. Handlers see to it that a logged message (carried as a [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord)) arrives at a specific place (or group of places) suited to the message's intended audience (for instance end users, support desk staff, system administrators, developers). Handlers receive `LogRecord` instances bound for particular destinations. A logger may have zero, one, or several handlers attached to it (via the [`addHandler()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.addHandler) method of [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger)). Beyond the handlers tied directly to a logger, *all handlers associated with all ancestors of the logger* are invoked to dispatch the message (unless that logger's *propagate* flag holds a false value, at which point delivery to ancestor handlers ceases).

Handlers, much like loggers, can carry their own levels. A handler's level filters in the very same fashion that a logger's level does. Once a handler resolves to actually dispatch an event, the [`emit()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.emit) method carries the message to its destination. The majority of user-defined [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) subclasses will have to override this `emit()`.

[Subject index](INDEX.md) · [Previous source context](configuring-logging-for-a-library.md) · [Following source context](custom-levels.md)
