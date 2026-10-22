# Subprocess Support on Windows

### Subprocess Support on Windows

On Windows, subprocesses work under the default event loop [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop), but not under [`SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop).

[Subject index](INDEX.md) · [Previous](windows.md) · [Continue](macos.md)
