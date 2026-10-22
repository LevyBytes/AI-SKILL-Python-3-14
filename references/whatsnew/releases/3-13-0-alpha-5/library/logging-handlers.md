# Python 3.13.0 alpha 5 / library / logging handlers

[gh-93205](https://github.com/python/cpython/issues/93205): Repair a defect in [`logging.handlers.TimedRotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler): several rotating handler instances aimed at files sharing a name but differing in extension would collide and remove the wrong files.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
