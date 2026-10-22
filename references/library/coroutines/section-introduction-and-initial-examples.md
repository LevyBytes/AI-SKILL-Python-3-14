# Coroutines — Section introduction and initial examples

### Coroutines

**Source code:** [Lib/asyncio/coroutines.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/coroutines.py)

---

Writing asyncio programs is best done with [Coroutines](https://docs.python.org/3.14/glossary.html#term-coroutine) built using the async/await syntax. As an illustration, the code below emits “hello”, pauses for 1 second, and afterward emits “world”:

```python
>>> import asyncio

>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')

>>> asyncio.run(main())
hello
world

```

Keep in mind that merely invoking a coroutine does not arrange for it to run:

```python
>>> main()
<coroutine object main at 0x1053bb7c8>

```

For a coroutine to genuinely execute, asyncio offers these approaches:

- Use [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) to launch the top-level entry point “main()” function (refer to the earlier example.)

- Awaiting on a coroutine. After a 1 second pause the code below prints “hello”, then following *another* 2 seconds it prints “world”:

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

```

Expected output:

```python
started at 17:13:52
hello
world
finished at 17:13:55

```

- The `asyncio.create_task()` function to run coroutines concurrently as asyncio `Tasks`.

Suppose we adjust the earlier example so that two `say_after` coroutines run *concurrently*:

[Subject index](INDEX.md) · [Previous](../asyncio-task/coroutines-and-tasks.md) · [Continue](code-example-async-def-main.md)
