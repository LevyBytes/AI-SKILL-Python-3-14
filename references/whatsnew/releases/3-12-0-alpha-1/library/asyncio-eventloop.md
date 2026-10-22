# Python 3.12.0 alpha 1 / library / asyncio eventloop

[bpo-38267](https://bugs.python.org/issue?@action=redirect&bpo=38267): A *timeout* parameter is now accepted by [`asyncio.loop.shutdown_default_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor). With its default of `None`, the executor is allotted an unbounded amount of time. Whenever the call originates from [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) or [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run), the timeout defaults to 5 minutes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
