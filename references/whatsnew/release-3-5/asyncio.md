# What’s New In Python 3.5 / asyncio - asyncio, asyncio-eventloop, asyncio-future, asyncio-protocol, asyncio-queue, asyncio-stream, asyncio-task

### asyncio

Because the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module remains [provisional](https://docs.python.org/3.14/glossary.html#term-provisional-API), every change that arrived in Python 3.5 was likewise backported into Python 3.4.x.

Noteworthy revisions within the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module since Python 3.4.0:

- Fresh debugging APIs: the [`loop.set_debug()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_debug) and [`loop.get_debug()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.get_debug) methods. (Contributed by Victor Stinner.)

- The proactor event loop has gained SSL support. (Contributed by Antoine Pitrou and Victor Stinner in [bpo-22560](https://bugs.python.org/issue?@action=redirect&bpo=22560).)

- A fresh [`loop.is_closed()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.is_closed) method reports whether the event loop has been closed. (Contributed by Victor Stinner in [bpo-21326](https://bugs.python.org/issue?@action=redirect&bpo=21326).)

- A fresh [`loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task) lets you conveniently build and schedule a fresh [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) around a coroutine. Every asyncio function that wraps coroutines into tasks, including [`asyncio.wait()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait), [`asyncio.gather()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.gather), and the like, also leans on the `create_task` method. (Contributed by Victor Stinner.)

- A fresh [`transport.get_write_buffer_limits()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_limits) method queries the *high-* and *low-* water marks governing flow control. (Contributed by Victor Stinner.)

- The `async()` function now stands deprecated, with [`ensure_future()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.ensure_future) taking its place. (Contributed by Yury Selivanov.)

- Fresh [`loop.set_task_factory()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_task_factory) and [`loop.get_task_factory()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.get_task_factory) methods let you tailor the task factory that the [`loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task) method relies upon. (Contributed by Yury Selivanov.)

- Fresh [`Queue.join()`](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio.Queue.join) and [`Queue.task_done()`](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio.Queue.task_done) queue methods. (Contributed by Victor Stinner.)

- The `JoinableQueue` class got removed, with the [`asyncio.Queue`](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio.Queue) class replacing it. (Contributed by Victor Stinner.)

Updates in 3.5.1:

- The [`ensure_future()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.ensure_future) function, together with every function building on it such as [`loop.run_until_complete()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_until_complete), will henceforth take any sort of [awaitable objects](https://docs.python.org/3.14/glossary.html#term-awaitable). (Contributed by Yury Selivanov.)

- A fresh [`run_coroutine_threadsafe()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.run_coroutine_threadsafe) function hands coroutines off to event loops running on other threads. (Contributed by Vincent Michel.)

- A fresh [`Transport.is_closing()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseTransport.is_closing) method tells you whether the transport sits closing or already closed. (Contributed by Yury Selivanov.)

- The [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server) method will henceforth take a list of hosts. (Contributed by Yann Sionneau.)

Updates in 3.5.2:

- A fresh [`loop.create_future()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_future) method builds Future objects. By doing so it permits alternative event loop implementations, [uvloop](https://github.com/MagicStack/uvloop) among them, to supply a quicker [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) implementation. (Contributed by Yury Selivanov.)

- A fresh [`loop.get_exception_handler()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.get_exception_handler) method retrieves whichever exception handler is currently set. (Contributed by Yury Selivanov.)

- A fresh [`StreamReader.readuntil()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader.readuntil) method pulls data off the stream right up until a separator byte sequence shows up. (Contributed by Mark Korenberg.)

- The [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection) plus [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server) methods were tuned to skip a call into the system `getaddrinfo` function whenever the address has already been resolved. (Contributed by A. Jesse Jiryu Davis.)

- The [`loop.sock_connect(sock, address)`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sock_connect) henceforth stops insisting that the *address* be resolved ahead of the call. (Contributed by A. Jesse Jiryu Davis.)

[Subject index](INDEX.md) · [Previous source section](argparse.md) · [Next source section](bz2.md) · [Release/subject declaration](summary-release-highlights.md)
