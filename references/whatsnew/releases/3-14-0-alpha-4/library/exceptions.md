# Python 3.14.0 alpha 4 / library / exceptions

[gh-128731](https://github.com/python/cpython/issues/128731): Cleared a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) raised inside [`urllib.robotparser.RobotFileParser.read()`](https://docs.python.org/3.14/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.read).

[gh-127529](https://github.com/python/cpython/issues/127529): Set right the behavior of `asyncio.selector_events.BaseSelectorEventLoop._accept_connection()` as it handles [`ConnectionAbortedError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionAbortedError) within a loop. OpenBSD sees a performance gain from this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
