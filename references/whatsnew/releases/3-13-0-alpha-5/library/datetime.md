# Python 3.13.0 alpha 5 / library / datetime

[gh-115809](https://github.com/python/cpython/issues/115809): Sharpen the algorithm that figures out which rolled-over log files to delete in `logging.TimedRotatingFileHandler`. It is now dependable for handlers lacking a `namer` as well as with any deterministic `namer` that keeps the datetime portion of the file name untouched.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
