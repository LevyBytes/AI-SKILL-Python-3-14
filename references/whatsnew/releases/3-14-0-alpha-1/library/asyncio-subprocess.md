# Python 3.14.0 alpha 1 / library / asyncio subprocess

[gh-87744](https://github.com/python/cpython/issues/87744): Repair a waitpid race that surfaced when [`send_signal()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.subprocess.Process.send_signal) was called in asyncio. Patch by Kumar Aditya.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
