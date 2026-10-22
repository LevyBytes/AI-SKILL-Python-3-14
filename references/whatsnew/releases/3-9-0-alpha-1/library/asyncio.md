# Python 3.9.0 alpha 1 / library / asyncio

[bpo-38148](https://bugs.python.org/issue?@action=redirect&bpo=38148): Slots were added to the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) transport classes, which can trim memory usage.

[bpo-34037](https://bugs.python.org/issue?@action=redirect&bpo=34037): For [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio), a new coroutine `loop.shutdown_default_executor()` was introduced. This coroutine offers an API for scheduling an executor shutdown that blocks until the threadpool has finished closing. In addition, [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) was reworked to make use of the new coroutine. Kyle Stanley wrote the patch.

[bpo-37279](https://bugs.python.org/issue?@action=redirect&bpo=37279): Corrected asyncio sendfile handling for the case where sendfile pushes extra data during fallback mode.

[bpo-35621](https://bugs.python.org/issue?@action=redirect&bpo=35621): On UNIX, asyncio subprocesses may now run while the event loop executes inside a thread.

[bpo-38242](https://bugs.python.org/issue?@action=redirect&bpo=38242): Reverted the new asyncio Streams API

[bpo-38019](https://bugs.python.org/issue?@action=redirect&bpo=38019): Pause and resume of reading on a closed asyncio unix pipe is now handled correctly.

[bpo-38248](https://bugs.python.org/issue?@action=redirect&bpo=38248): asyncio: Corrected inconsistent immediate Task cancellation

[bpo-38785](https://bugs.python.org/issue?@action=redirect&bpo=38785): Stop asyncio from crashing whenever a parent `__init__` goes uncalled from the constructor of an object derived from `asyncio.Future`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
