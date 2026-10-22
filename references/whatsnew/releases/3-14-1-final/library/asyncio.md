# Python 3.14.1 final / library / asyncio

[gh-139845](https://github.com/python/cpython/issues/139845): Stops the default asyncio REPL from printing KeyboardInterrupt twice.

[gh-139391](https://github.com/python/cpython/issues/139391): Resolves a case on non-Windows platforms where a `python -m asyncio` process, once suspended via Ctrl+Z and afterward brought back by *[fg](https://manpages.debian.org/fg)*, could not be exited cleanly by any means besides *[kill](https://manpages.debian.org/kill)*.

[gh-139894](https://github.com/python/cpython/issues/139894): Stops the current task from being incorrectly shared with the child process during a fork in [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio). Kumar Aditya authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
