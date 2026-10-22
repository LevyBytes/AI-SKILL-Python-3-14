# Python 3.13.0 alpha 3 / library / signal

[gh-112559](https://github.com/python/cpython/issues/112559): Callable handlers are no longer passed through `repr` by [`signal.signal()`](https://docs.python.org/3.14/library/signal.html#signal.signal) and [`signal.getsignal()`](https://docs.python.org/3.14/library/signal.html#signal.getsignal). Likewise, task results are no longer fed to `repr` by [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) and [`asyncio.Runner.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner.run). Yilei Yang wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
