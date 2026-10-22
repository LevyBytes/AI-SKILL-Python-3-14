# Python 3.12.0 alpha 1 / library / threads and concurrency

[gh-96349](https://github.com/python/cpython/issues/96349): A small performance regression affecting `threading.Event.__init__()` is resolved.

[gh-94637](https://github.com/python/cpython/issues/94637): `SSLContext.set_default_verify_paths()` now drops the GIL while the `SSL_CTX_set_default_verify_paths` call runs. That call carries out I/O along with CPU intensive work.

[gh-94182](https://github.com/python/cpython/issues/94182): execute the `asyncio.PidfdChildWatcher` against whichever loop is currently running, which lets event loops launch subprocesses even with no default event loop active on the main thread

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
