# What's new in Python 3.14 / asyncio — asyncio-eventloop, asyncio-runner, asyncio-sync

### asyncio

- Drop the classes, methods, and functions listed below, all deprecated since Python 3.12:

  - `AbstractChildWatcher`

  - `FastChildWatcher`

  - `MultiLoopChildWatcher`

  - `PidfdChildWatcher`

  - `SafeChildWatcher`

  - `ThreadedChildWatcher`

  - `AbstractEventLoopPolicy.get_child_watcher()`

  - `AbstractEventLoopPolicy.set_child_watcher()`

  - `get_child_watcher()`

  - `set_child_watcher()`

(Contributed by Kumar Aditya in [gh-120804](https://github.com/python/cpython/issues/120804).)

- [`asyncio.get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) now raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) whenever no current event loop exists, and it no longer creates an event loop implicitly.

(Contributed by Kumar Aditya in [gh-126353](https://github.com/python/cpython/issues/126353).)

A handful of patterns lean on [`asyncio.get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop), and most can swap in [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run).

When you are running an async function, just call [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run).

Before:

```python
async def main():
    ...

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

```

After:

```python
async def main():
    ...

asyncio.run(main())

```

When you need to launch something, say a server listening on a socket, and then keep running indefinitely, lean on [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) together with an [`asyncio.Event`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Event).

[Subject index](INDEX.md) · [Previous source section](ast.md) · [Next source section](asyncio-runner-migration.md) · [Release/subject declaration](summary-release-highlights.md)
