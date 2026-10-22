# Windows

### Windows

**Source code:** [Lib/asyncio/proactor_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/proactor_events.py), [Lib/asyncio/windows_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/windows_events.py), [Lib/asyncio/windows_utils.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/windows_utils.py)

---

Changed in version 3.8: Under Windows, the default event loop is now [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop).

On Windows, none of the event loops support the methods below:

- [`loop.create_unix_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection) and [`loop.create_unix_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_server) are unsupported. The [`socket.AF_UNIX`](https://docs.python.org/3.14/library/socket.html#socket.AF_UNIX) socket family belongs to Unix.

- [`loop.add_signal_handler()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler) and [`loop.remove_signal_handler()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.remove_signal_handler) are unsupported.

[`SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) comes with the limitations below:

- [`SelectSelector`](https://docs.python.org/3.14/library/selectors.html#selectors.SelectSelector) handles waiting on socket events: it works with sockets and tops out at 512 sockets.

- [`loop.add_reader()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.add_reader) and [`loop.add_writer()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.add_writer) take only socket handles (so, for instance, pipe file descriptors are unsupported).

- Because pipes are unsupported, the [`loop.connect_read_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe) and [`loop.connect_write_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe) methods go unimplemented.

- [Subprocesses](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio-subprocess) are unsupported, meaning the [`loop.subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec) and [`loop.subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell) methods go unimplemented.

[`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) comes with the limitations below:

- The [`loop.add_reader()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.add_reader) and [`loop.add_writer()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.add_writer) methods are unsupported.

On Windows the monotonic clock typically resolves to roughly 15.6 milliseconds. Its finest resolution is 0.5 milliseconds. What resolution you get hinges on the hardware (whether [HPET](https://en.wikipedia.org/wiki/High_Precision_Event_Timer) is present) and on how Windows is configured.

[Subject index](INDEX.md) · [Previous](all-platforms.md) · [Continue](subprocess-support-on-windows.md)
