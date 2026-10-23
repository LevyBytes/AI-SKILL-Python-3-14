# What's new in Python 3.14 / asyncio - asyncio-runner

Before:

```python
def start_server(loop): ...

loop = asyncio.get_event_loop()
try:
    start_server(loop)
    loop.run_forever()
finally:
    loop.close()

```

After:

```python
def start_server(loop): ...

async def main():
    start_server(asyncio.get_running_loop())
    await asyncio.Event().wait()

asyncio.run(main())

```

When you need to run something inside an event loop, then run some blocking code around it, lean on [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner).

Before:

[Subject index](INDEX.md) · [Previous source section](asyncio-main-and-main.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](asyncio-main-and-main.md) · [Following release/subject continuation](asyncio-blocking-code-migration.md)
