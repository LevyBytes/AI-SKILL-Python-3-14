# Python 3.12.0 alpha 1 / library / logging

[gh-89258](https://github.com/python/cpython/issues/89258): A [`getChildren()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.getChildren) method now exists on [`logging.Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) so you can fetch a logger's direct child loggers.

[gh-96159](https://github.com/python/cpython/issues/96159): A logging performance regression in TimedRotatingFileHandler is fixed. Special files get checked only once the rollover moment has elapsed.

[gh-95804](https://github.com/python/cpython/issues/95804): The `logging` shutdown handler is fixed so it honors `MemoryHandler.flushOnClose`.

[gh-91513](https://github.com/python/cpython/issues/91513): Gave the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module a `taskName` attribute meant for use alongside [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) tasks.

[gh-92591](https://github.com/python/cpython/issues/92591): Let [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) filters hand back a [`logging.LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) instance, so that filters fastened to [`logging.Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler)s can augment records without affecting other handlers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
