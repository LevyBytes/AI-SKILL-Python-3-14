# Python 3.13.0 alpha 5 / library / files and paths

[gh-88352](https://github.com/python/cpython/issues/88352): Repair how the next rollover time gets computed inside the `logging.TimedRotatingFileHandler` handler. `computeRollover()` now consistently yields a timestamp past the given time and behaves right across a DST change. `doRollover()` no longer clobbers the file that already rolled over, sparing data from loss when it runs at midnight or during the repeated hour at the DST change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
