# What's New In Python 3.11 / asyncio - asyncio-eventloop, asyncio-runner, asyncio-stream, asyncio-sync, asyncio-task

### Improved Modules

### asyncio

- The [`TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) class arrived as an [asynchronous context manager](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers) that gathers a bundle of tasks and blocks until each finishes when it exits. Fresh code should reach for it ahead of calling [`create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) and [`gather()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.gather) directly. (Contributed by Yury Selivanov and others in [gh-90908](https://github.com/python/cpython/issues/90908).)

- [`timeout()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.timeout) was added: an asynchronous context manager that applies a timeout across asynchronous work. Fresh code should favor it rather than reaching for [`wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) directly. (Contributed by Andrew Svetlov in [gh-90927](https://github.com/python/cpython/issues/90927).)

- The [`Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) class was added, surfacing the internal mechanism that backs [`run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run). (Contributed by Andrew Svetlov in [gh-91218](https://github.com/python/cpython/issues/91218).)

- The [`Barrier`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Barrier) class joined asyncio's synchronization primitives, paired with the matching [`BrokenBarrierError`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.BrokenBarrierError) exception. (Contributed by Yves Duprat and Andrew Svetlov in [gh-87518](https://github.com/python/cpython/issues/87518).)

- A keyword argument *all_errors* now exists on [`asyncio.loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection), letting several connection failures surface together as an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup).

- The [`asyncio.StreamWriter.start_tls()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter.start_tls) method was added to promote already-open stream connections to TLS. (Contributed by Ian Good in [bpo-34975](https://bugs.python.org/issue?@action=redirect&bpo=34975).)

- The event loop gained low-level datagram socket helpers: [`sock_sendto()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sock_sendto), [`sock_recvfrom()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom) and [`sock_recvfrom_into()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom_into). Both [`SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) and [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) carry implementations of them. (Contributed by Alex Grönholm in [bpo-46805](https://bugs.python.org/issue?@action=redirect&bpo=46805).)

- [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) picked up [`cancelling()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancelling) and [`uncancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.uncancel) methods. They mainly serve internal callers, especially [`TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup).

[Subject index](INDEX.md) · [Previous source section](new-modules.md) · [Next source section](contextlib.md) · [Release/subject declaration](summary-release-highlights.md)
