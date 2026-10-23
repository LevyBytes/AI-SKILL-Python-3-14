# asyncio - Close asynchronous generators explicitly

### Close asynchronous generators explicitly

The advice is to close the [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator-iterator) yourself, by hand. Where a generator bows out early — say because an exception fired inside the body of an `async for` loop — its asynchronous cleanup code might end up executing in a context you didn’t expect. That can land after the tasks it relies on have wrapped up, or amid the event loop shutdown, the moment the async-generator’s garbage collection hook fires.

Sidestep this by closing the generator outright: call its [`aclose()`](https://docs.python.org/3.14/reference/expressions.html#agen.aclose) method, or wrap it in the [`contextlib.aclosing()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.aclosing) context manager:

```python
import asyncio
import contextlib

async def gen():
  yield 1
  yield 2

async def func():
  async with contextlib.aclosing(gen()) as g:
    async for x in g:
      break  # Don't iterate until the end

asyncio.run(func())

```

Per the point made above, the cleanup code belonging to these asynchronous generators gets put off. The example below shows how an asynchronous generator’s finalization may happen out of the order you would expect:

```python
import asyncio
work_done = False

async def cursor():
    try:
        yield 1
    finally:
        assert work_done

async def rows():
    global work_done
    try:
        yield 2
    finally:
        await asyncio.sleep(0.1) # immitate some async work
        work_done = True

async def main():
    async for c in cursor():
        async for r in rows():
            break
        break

asyncio.run(main())

```

Running this example yields the output below:

```python
unhandled exception during asyncio.run() shutdown
task: <Task finished name='Task-3' coro=<<async_generator_athrow without __name__>()> exception=AssertionError()>
Traceback (most recent call last):
  File "example.py", line 6, in cursor
    yield 1
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "example.py", line 8, in cursor
    assert work_done
           ^^^^^^^^^
AssertionError

```

Here the `cursor()` asynchronous generator wound up finalized ahead of the `rows` generator — behavior you wouldn’t anticipate.

You can set the example right by closing the `cursor` and `rows` async-generators yourself:

```python
async def main():
    async with contextlib.aclosing(cursor()) as cursor_gen:
        async for c in cursor_gen:
            async with contextlib.aclosing(rows()) as rows_gen:
                async for r in rows_gen:
                    break
            break

```

[Subject index](INDEX.md) · [Previous](asynchronous-generators-best-practices.md) · [Continue](async-generator-event-loop-lifecycle.md)
