# Python 3.12.0 alpha 1 / library / asyncio runner

[gh-95097](https://github.com/python/cpython/issues/95097): [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) is fixed for [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) implementations that omit the [`uncancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.uncancel) method. Kumar Aditya wrote the patch.

[gh-95899](https://github.com/python/cpython/issues/95899): [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) is corrected so it invokes [`asyncio.set_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.set_event_loop) just a single time, keeping `attach_loop()` from running repeatedly against child watchers. Kumar Aditya wrote the patch.

[gh-93896](https://github.com/python/cpython/issues/93896): [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) plus [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase) are fixed to always set the event loop, matching how Python 3.10 and earlier behaved. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
