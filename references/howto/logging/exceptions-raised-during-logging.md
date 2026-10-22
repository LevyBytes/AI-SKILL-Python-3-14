# Exceptions raised during logging

### Exceptions raised during logging

The logging package deliberately suppresses exceptions that arise while logging in production. The aim is to keep errors that occur while handling logging events - such as logging misconfiguration, network problems, or similar failures - from causing the application that relies on logging to exit too soon.

[`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) and [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exceptions are never suppressed. Any other exception raised during the [`emit()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.emit) method of a [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) subclass is forwarded to its [`handleError()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.handleError) method.

Within [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler), the default implementation of [`handleError()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.handleError) tests whether a module-level variable, [`raiseExceptions`](https://docs.python.org/3.14/library/logging.html#logging.raiseExceptions), is set. When it is set, a traceback gets printed to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr). When it is not set, the exception is suppressed.

Note

[`raiseExceptions`](https://docs.python.org/3.14/library/logging.html#logging.raiseExceptions) defaults to `True`. That is because during development you normally want to learn about any exceptions that arise. The recommendation is to set `raiseExceptions` to `False` for production usage.

[Subject index](INDEX.md) · [Following source continuation](logging-arbitrary-objects-as-messages.md) · [Previous source context](useful-handlers.md) · [Following source context](logging-arbitrary-objects-as-messages.md)
