# What's New In Python 3.7 / asyncio — asyncio, asyncio-eventloop, asyncio-future, asyncio-protocol, asyncio-runner, asyncio-stream, asyncio-task, contextvars, os

### asyncio

Plenty of fresh capabilities, plus usability and speed gains, landed in the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module. Among the noteworthy updates:

- A fresh [provisional](https://docs.python.org/3.14/glossary.html#term-provisional-API) [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) function lets you execute a coroutine from synchronous code, since it builds and tears down the event loop for you. (Contributed by Yury Selivanov in [bpo-32314](https://bugs.python.org/issue?@action=redirect&bpo=32314).)

- asyncio picked up [`contextvars`](https://docs.python.org/3.14/library/contextvars.html#module-contextvars) support. A new optional keyword-only *context* parameter was added to [`loop.call_soon()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon), [`loop.call_soon_threadsafe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe), [`loop.call_later()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_later), [`loop.call_at()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_at), and [`Future.add_done_callback()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.add_done_callback). Their context is now tracked automatically by [`Tasks`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task). Consult [**PEP 567**](https://peps.python.org/pep-0567/) for further specifics. (Contributed by Yury Selivanov in [bpo-32436](https://bugs.python.org/issue?@action=redirect&bpo=32436).)

- A fresh [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) function arrived as a shorthand for `asyncio.get_event_loop().create_task()`. (Contributed by Andrew Svetlov in [bpo-32311](https://bugs.python.org/issue?@action=redirect&bpo=32311).)

- A fresh [`loop.start_tls()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.start_tls) method lets you promote a live connection to TLS. (Contributed by Yury Selivanov in [bpo-23749](https://bugs.python.org/issue?@action=redirect&bpo=23749).)

- A fresh [`loop.sock_recv_into()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sock_recv_into) method reads bytes off a socket straight into a caller-supplied buffer, which cuts down on data copying. (Contributed by Antoine Pitrou in [bpo-31819](https://bugs.python.org/issue?@action=redirect&bpo=31819).)

- A fresh [`asyncio.current_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.current_task) function yields the [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) instance executing right now, and a fresh [`asyncio.all_tasks()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.all_tasks) function yields a set holding every `Task` instance that lives in the given loop. Deprecation now applies to the `Task.current_task()` and `Task.all_tasks()` methods. (Contributed by Andrew Svetlov in [bpo-32250](https://bugs.python.org/issue?@action=redirect&bpo=32250).)

- A fresh *provisional* [`BufferedProtocol`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BufferedProtocol) class lets you write streaming protocols while keeping hands-on control of the receive buffer. (Contributed by Yury Selivanov in [bpo-32251](https://bugs.python.org/issue?@action=redirect&bpo=32251).)

- A fresh [`asyncio.get_running_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_running_loop) function gives back the loop running at the moment, throwing a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) when nothing is running. Compare that to [`asyncio.get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop), which goes ahead and *creates* a fresh event loop if none happens to be running. (Contributed by Yury Selivanov in [bpo-32269](https://bugs.python.org/issue?@action=redirect&bpo=32269).)

- A fresh [`StreamWriter.wait_closed()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter.wait_closed) coroutine method lets you block until the stream writer finishes closing. The fresh [`StreamWriter.is_closing()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter.is_closing) method tells you whether the writer is in the process of closing. (Contributed by Andrew Svetlov in [bpo-32391](https://bugs.python.org/issue?@action=redirect&bpo=32391).)

- A fresh [`loop.sock_sendfile()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sock_sendfile) coroutine method transmits files via [`os.sendfile`](https://docs.python.org/3.14/library/os.html#os.sendfile) where that is available. (Contributed by Andrew Svetlov in [bpo-32410](https://bugs.python.org/issue?@action=redirect&bpo=32410).)

- Fresh [`Future.get_loop()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.get_loop) and `Task.get_loop()` methods hand back the loop instance that a future or task was built on. [`Server.get_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.get_loop) offers the equivalent for [`asyncio.Server`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server) objects. (Contributed by Yury Selivanov in [bpo-32415](https://bugs.python.org/issue?@action=redirect&bpo=32415) and Srinivas Reddy Thatiparthy in [bpo-32418](https://bugs.python.org/issue?@action=redirect&bpo=32418).)

- You can now govern the way instances of [`asyncio.Server`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server) start accepting clients. In the past the server would begin serving the instant it was created. A fresh *start_serving* keyword argument on [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server) and [`loop.create_unix_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_server), together with [`Server.start_serving()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.start_serving) and [`Server.serve_forever()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.serve_forever), lets you split apart creating the server from serving on it. A fresh [`Server.is_serving()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.is_serving) method gives back `True` while the server is serving. `Server` objects now act as asynchronous context managers:

```python
srv = await loop.create_server(...)

async with srv:
    # some code

# At this point, srv is closed and no longer accepts new connections.

```

(Contributed by Yury Selivanov in [bpo-32662](https://bugs.python.org/issue?@action=redirect&bpo=32662).)

- The callback objects handed back from [`loop.call_later()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_later) picked up a fresh [`when()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.TimerHandle.when) method that reports the absolute timestamp the callback is scheduled for. (Contributed by Andrew Svetlov in [bpo-32741](https://bugs.python.org/issue?@action=redirect&bpo=32741).)

- Unix sockets are now handled by the [`loop.create_datagram_endpoint() `](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) method. (Contributed by Quentin Dawans in [bpo-31245](https://bugs.python.org/issue?@action=redirect&bpo=31245).)

- A *ssl_handshake_timeout* keyword argument is now taken by the [`asyncio.open_connection()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.open_connection), [`asyncio.start_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_server) functions, the [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection), [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server), [`loop.create_accepted_socket()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket) methods along with their matching UNIX socket counterparts. (Contributed by Neil Aspinall in [bpo-29970](https://bugs.python.org/issue?@action=redirect&bpo=29970).)

- A fresh [`Handle.cancelled()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Handle.cancelled) method reports `True` once the callback has been cancelled. (Contributed by Marat Sharafutdinov in [bpo-31943](https://bugs.python.org/issue?@action=redirect&bpo=31943).)

- The codebase behind asyncio was migrated over to the [`async`](https://docs.python.org/3.14/reference/compound_stmts.html#async)/[`await`](https://docs.python.org/3.14/reference/expressions.html#await) syntax. (Contributed by Andrew Svetlov in [bpo-32193](https://bugs.python.org/issue?@action=redirect&bpo=32193).)

- A fresh [`ReadTransport.is_reading()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.ReadTransport.is_reading) method lets you query whether the transport is currently reading. On top of that, invoking [`ReadTransport.resume_reading()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.ReadTransport.resume_reading) and [`ReadTransport.pause_reading()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.ReadTransport.pause_reading) is idempotent now. (Contributed by Yury Selivanov in [bpo-32356](https://bugs.python.org/issue?@action=redirect&bpo=32356).)

- Loop methods that take socket paths will accept [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) now. (Contributed by Yury Selivanov in [bpo-32066](https://bugs.python.org/issue?@action=redirect&bpo=32066).)

- Within [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio), TCP sockets running on Linux now get the `TCP_NODELAY` flag turned on by default. (Contributed by Yury Selivanov and Victor Stinner in [bpo-27456](https://bugs.python.org/issue?@action=redirect&bpo=27456).)

- When a task is cancelled, exceptions raised inside it are no longer written to the log. (Contributed by Yury Selivanov in [bpo-30508](https://bugs.python.org/issue?@action=redirect&bpo=30508).)

- New `WindowsSelectorEventLoopPolicy` and `WindowsProactorEventLoopPolicy` classes. (Contributed by Yury Selivanov in [bpo-33792](https://bugs.python.org/issue?@action=redirect&bpo=33792).)

A number of `asyncio` APIs have now been deprecated.

### asyncio

Directly `await`-ing instances of [`asyncio.Lock`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Lock) and the other asyncio synchronization primitives is now deprecated. To acquire and then release such a synchronization resource, an asynchronous context manager has to be used. (Contributed by Andrew Svetlov in [bpo-32253](https://bugs.python.org/issue?@action=redirect&bpo=32253).)

Deprecation also applies to the `asyncio.Task.current_task()` and `asyncio.Task.all_tasks()` methods. (Contributed by Andrew Svetlov in [bpo-32250](https://bugs.python.org/issue?@action=redirect&bpo=32250).)

[Subject index](INDEX.md) · [Previous source section](argparse.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](binascii.md) · [Previous source section](aifc.md) · [Next source section](collections.md)
