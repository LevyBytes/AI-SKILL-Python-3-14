# asyncio - Detect never-retrieved exceptions

### Detect never-retrieved exceptions

Should [`Future.set_exception()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.set_exception) be invoked while the Future object is never awaited, that exception simply never reaches your code. When that happens, asyncio writes a log message at the point the Future object is garbage collected.

An unhandled-exception example:

```python
import asyncio

async def bug():
    raise Exception("not consumed")

async def main():
    asyncio.create_task(bug())

asyncio.run(main())

```

Output:

```python
Task exception was never retrieved
future: <Task finished coro=<bug() done, defined at test.py:3>
  exception=Exception('not consumed')>

Traceback (most recent call last):
  File "test.py", line 4, in bug
    raise Exception("not consumed")
Exception: not consumed

```

Switch the debug mode on to surface the traceback marking where the task was created:

```python
asyncio.run(main(), debug=True)

```

Output in debug mode:

```python
Task exception was never retrieved
future: <Task finished coro=<bug() done, defined at test.py:3>
    exception=Exception('not consumed') created at asyncio/tasks.py:321>

source_traceback: Object created at (most recent call last):
  File "../t.py", line 9, in <module>
    asyncio.run(main(), debug=True)

< .. >

Traceback (most recent call last):
  File "../t.py", line 4, in bug
    raise Exception("not consumed")
Exception: not consumed

```

[Subject index](INDEX.md) · [Previous](detect-never-awaited-coroutines.md) · [Continue](asynchronous-generators-best-practices.md)
