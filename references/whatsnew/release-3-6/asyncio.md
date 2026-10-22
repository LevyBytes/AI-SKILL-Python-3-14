# What's New In Python 3.6 / asyncio — asyncio, asyncio-eventloop, asyncio-future, asyncio-protocol, asyncio-stream, asyncio-task

### asyncio

From Python 3.6 onward the `asyncio` module sheds its provisional label and its API counts as stable.

Worth noting are these revisions to the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module made since Python 3.5.0 (every one backported into 3.5.x given the provisional status):

- The [`get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) function now always hands back the loop currently running whenever it is invoked from coroutines and callbacks. (Contributed by Yury Selivanov in [bpo-28613](https://bugs.python.org/issue?@action=redirect&bpo=28613).)

- The [`ensure_future()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.ensure_future) function, along with everything built on it such as [`loop.run_until_complete()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_until_complete), now takes every variety of [awaitable objects](https://docs.python.org/3.14/glossary.html#term-awaitable). (Contributed by Yury Selivanov.)

- A new [`run_coroutine_threadsafe()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.run_coroutine_threadsafe) function for handing coroutines to event loops out of separate threads. (Contributed by Vincent Michel.)

- A new [`Transport.is_closing()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseTransport.is_closing) method for testing whether the transport is in the process of closing or already closed. (Contributed by Yury Selivanov.)

- The [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server) method is now capable of taking a list of hosts. (Contributed by Yann Sionneau.)

- A new [`loop.create_future()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_future) method for building Future objects. With it, substitute event loop implementations, [uvloop](https://github.com/MagicStack/uvloop) among them, can supply a quicker [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) implementation. (Contributed by Yury Selivanov in [bpo-27041](https://bugs.python.org/issue?@action=redirect&bpo=27041).)

- A new [`loop.get_exception_handler()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.get_exception_handler) method for retrieving the exception handler currently in place. (Contributed by Yury Selivanov in [bpo-27040](https://bugs.python.org/issue?@action=redirect&bpo=27040).)

- A new [`StreamReader.readuntil()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader.readuntil) method that pulls data off the stream right up until a separator bytes sequence shows up. (Contributed by Mark Korenberg.)

- The speed of [`StreamReader.readexactly()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader.readexactly) has gotten better. (Contributed by Mark Korenberg in [bpo-28370](https://bugs.python.org/issue?@action=redirect&bpo=28370).)

- The [`loop.getaddrinfo()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo) method now skips invoking the system `getaddrinfo` function whenever the address has already been resolved. (Contributed by A. Jesse Jiryu Davis.)

- The [`loop.stop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.stop) method now halts the loop right after the iteration in progress. Whatever fresh callbacks the final iteration queues up get thrown away. (Contributed by Guido van Rossum in [bpo-25593](https://bugs.python.org/issue?@action=redirect&bpo=25593).)

- [`Future.set_exception`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.set_exception) now throws [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) if it receives an instance of the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception. (Contributed by Chris Angelico in [bpo-26221](https://bugs.python.org/issue?@action=redirect&bpo=26221).)

- A new [`loop.connect_accepted_socket()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket) method intended for servers that take in connections beyond asyncio yet still lean on asyncio to service them. (Contributed by Jim Fulton in [bpo-27392](https://bugs.python.org/issue?@action=redirect&bpo=27392).)

- The `TCP_NODELAY` flag now applies to every TCP transport out of the box. (Contributed by Yury Selivanov in [bpo-27456](https://bugs.python.org/issue?@action=redirect&bpo=27456).)

- A new [`loop.shutdown_asyncgens()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens) for cleanly finishing any outstanding asynchronous generators ahead of shutting the loop down. (Contributed by Yury Selivanov in [bpo-28003](https://bugs.python.org/issue?@action=redirect&bpo=28003).)

- The [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) and [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) classes have gained a tuned C implementation that speeds up asyncio code by as much as 30%. (Contributed by Yury Selivanov and INADA Naoki in [bpo-26081](https://bugs.python.org/issue?@action=redirect&bpo=26081) and [bpo-28544](https://bugs.python.org/issue?@action=redirect&bpo=28544).)

[Subject index](INDEX.md) · [Previous source section](ast.md) · [Next source section](binascii.md) · [Release/subject declaration](summary-release-highlights.md)
