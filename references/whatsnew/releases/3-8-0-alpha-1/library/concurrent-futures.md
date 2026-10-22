# Python 3.8.0 alpha 1 / library / concurrent futures

[bpo-33238](https://bugs.python.org/issue?@action=redirect&bpo=33238): Added `InvalidStateError` into [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures). `Future.set_result` and `Future.set_exception` now raise `InvalidStateError` whenever the futures are neither pending nor running. Patch by Jason Haydaman.

[bpo-34622](https://bugs.python.org/issue?@action=redirect&bpo=34622): Introduced dedicated `asyncio.CancelledError`, `asyncio.InvalidStateError` and `asyncio.TimeoutError` exception classes, each inheriting from the matching exception in the `concurrent.futures` package, and pulled the `asyncio` exceptions out into their own file.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
