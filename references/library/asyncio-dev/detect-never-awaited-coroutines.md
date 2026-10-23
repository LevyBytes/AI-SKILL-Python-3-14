# asyncio - Detect never-awaited coroutines

### Detect never-awaited coroutines

Call a coroutine function yet never await it — writing `coro()` rather than `await coro()` — or leave the coroutine unscheduled by [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task), and asyncio responds with a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning):

```python
import asyncio

async def test():
    print("never scheduled")

async def main():
    test()

asyncio.run(main())

```

Output:

```python
test.py:7: RuntimeWarning: coroutine 'test' was never awaited
  test()

```

Output in debug mode:

```python
test.py:7: RuntimeWarning: coroutine 'test' was never awaited
Coroutine created at (most recent call last)
  File "../t.py", line 9, in <module>
    asyncio.run(main(), debug=True)

  < .. >

  File "../t.py", line 7, in main
    test()
  test()

```

Typically you patch this by awaiting the coroutine, or else invoking the [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) function:

```python
async def main():
    await test()

```

[Subject index](INDEX.md) · [Previous](logging.md) · [Continue](detect-never-retrieved-exceptions.md)
