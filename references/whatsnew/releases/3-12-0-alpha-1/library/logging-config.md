# Python 3.12.0 alpha 1 / library / logging config

[gh-93162](https://github.com/python/cpython/issues/93162): Grant [`logging.config.dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) the means to meaningfully wire up [`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler) and [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) together as a pair, plus add the [`logging.getHandlerByName()`](https://docs.python.org/3.14/library/logging.html#logging.getHandlerByName) and [`logging.getHandlerNames()`](https://docs.python.org/3.14/library/logging.html#logging.getHandlerNames) APIs that fetch handlers by name.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
