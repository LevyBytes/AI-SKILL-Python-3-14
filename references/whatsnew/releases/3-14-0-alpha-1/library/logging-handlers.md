# Python 3.14.0 alpha 1 / library / logging handlers

[gh-105623](https://github.com/python/cpython/issues/105623): A performance regression in [`logging.handlers.RotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.RotatingFileHandler) is fixed. Craig Robson wrote the patch.

[gh-116263](https://github.com/python/cpython/issues/116263): An empty log file will no longer trigger a rollover from [`logging.handlers.RotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.RotatingFileHandler).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
