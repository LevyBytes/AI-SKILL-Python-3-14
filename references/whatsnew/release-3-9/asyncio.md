# What's New In Python 3.9 / asyncio - asyncio, asyncio-eventloop, asyncio-runner, asyncio-task, concurrent.futures, ssl

### asyncio

Owing to serious security worries, the *reuse_address* parameter belonging to [`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) is dropped. The reason is the way the `SO_REUSEADDR` socket option acts under UDP. Further specifics appear in the documentation covering `loop.create_datagram_endpoint()`. (Contributed by Kyle Stanley, Antoine Pitrou, and Yury Selivanov in [bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).)

A fresh [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) named [`shutdown_default_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor) was added; it queues a shutdown of the default executor and blocks until the [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) wraps up closing. Additionally, [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) was revised to call the new coroutine. (Contributed by Kyle Stanley in [bpo-34037](https://bugs.python.org/issue?@action=redirect&bpo=34037).)

Added `asyncio.PidfdChildWatcher`, a Linux-specific child watcher implementation that polls process file descriptors. ([bpo-38692](https://bugs.python.org/issue?@action=redirect&bpo=38692))

A fresh [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) named [`asyncio.to_thread()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.to_thread) was added. Its primary purpose is executing IO-bound callables on a distinct thread so the event loop stays unblocked, and at heart it behaves as a high-level form of [`run_in_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) that accepts keyword arguments directly. (Contributed by Kyle Stanley and Yury Selivanov in [bpo-32309](https://bugs.python.org/issue?@action=redirect&bpo=32309).)

On cancelling a task because of a timeout, [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) now holds off until the cancellation finishes even where *timeout* is <= 0, matching how it behaves under positive timeouts. (Contributed by Elvis Pranskevichus in [bpo-32751](https://bugs.python.org/issue?@action=redirect&bpo=32751).)

[`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) now raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) whenever incompatible methods get called against an [`ssl.SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) socket. (Contributed by Ido Michael in [bpo-37404](https://bugs.python.org/issue?@action=redirect&bpo=37404).)

[Subject index](INDEX.md) · [Previous source section](ast.md) · [Next source section](compileall.md) · [Release/subject declaration](summary-release-highlights.md)
