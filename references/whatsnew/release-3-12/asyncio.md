# What’s New In Python 3.12 / asyncio - asyncio, asyncio-runner, asyncio-task, os, socket

### asyncio

- Socket-writing throughput in [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) has improved by a wide margin. `asyncio` now sidesteps needless copies during socket writes and reaches for [`sendmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendmsg) wherever the platform offers it. (Contributed by Kumar Aditya in [gh-91166](https://github.com/python/cpython/issues/91166).)

- Add [`asyncio.eager_task_factory()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.eager_task_factory) plus [`asyncio.create_eager_task_factory()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_eager_task_factory) so that an event loop can be opted into eager task execution, which speeds certain workloads up 2x to 5x. (Contributed by Jacob Bower & Itamar Oren in [gh-102853](https://github.com/python/cpython/issues/102853), [gh-104140](https://github.com/python/cpython/issues/104140), and [gh-104138](https://github.com/python/cpython/issues/104138))

- Under Linux, [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) defaults to `asyncio.PidfdChildWatcher` whenever [`os.pidfd_open()`](https://docs.python.org/3.14/library/os.html#os.pidfd_open) exists and works, in place of `asyncio.ThreadedChildWatcher`. (Contributed by Kumar Aditya in [gh-98024](https://github.com/python/cpython/issues/98024).)

- For every platform the event loop now selects whichever child watcher is best (`asyncio.PidfdChildWatcher` where it is supported, otherwise `asyncio.ThreadedChildWatcher`), so setting up a child watcher by hand is discouraged. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

- Add a *loop_factory* parameter on [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) that lets you supply a bespoke event loop factory. (Contributed by Kumar Aditya in [gh-99388](https://github.com/python/cpython/issues/99388).)

- Add a C implementation of [`asyncio.current_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.current_task) yielding a 4x-6x speedup. (Contributed by Itamar Oren and Pranav Thulasiram Bhat in [gh-100344](https://github.com/python/cpython/issues/100344).)

- [`asyncio.iscoroutine()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.iscoroutine) hands back `False` for generators, since [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) provides no support for the older generator-based coroutines. (Contributed by Kumar Aditya in [gh-102748](https://github.com/python/cpython/issues/102748).)

- [`asyncio.wait()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait) along with [`asyncio.as_completed()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.as_completed) will now take generators that yield tasks. (Contributed by Kumar Aditya in [gh-78530](https://github.com/python/cpython/issues/78530).)

[Subject index](INDEX.md) · [Previous source section](array.md) · [Next source section](calendar.md) · [Release/subject declaration](summary-release-highlights.md)
