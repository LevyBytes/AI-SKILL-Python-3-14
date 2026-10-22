# What's new in Python 3.14 / configparser — configparser

### configparser

- To bolster security, `configparser` declines to write config files that it would be unable to read back. Calling [`write()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.write) with keys that hold delimiters or that open with the section header pattern now triggers an [`InvalidWriteError`](https://docs.python.org/3.14/library/configparser.html#configparser.InvalidWriteError). (Contributed by Jacob Lincoln in [gh-129270](https://github.com/python/cpython/issues/129270).)

[Subject index](INDEX.md) · [Previous source section](concurrent-futures.md) · [Next source section](contextvars.md) · [Release/subject declaration](summary-release-highlights.md)
