# Coroutines - Code example: async def main():

```python
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

```

Observe how the expected output now reveals that this snippet finishes a full second quicker than the earlier one:

```python
started at 17:14:32
hello
world
finished at 17:14:34

```

- As a newer option in place of `create_task()`, there is the `asyncio.TaskGroup` class. With it, the preceding example turns into:

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")

```

Both the timing and the output ought to match what the prior version produced.

Added in version 3.11: `asyncio.TaskGroup`.

[Subject index](INDEX.md) · [Previous](section-introduction-and-initial-examples.md) · [Continue](../asyncio-task/awaitables.md) · [Owning module, declaration or section: Coroutines](section-introduction-and-initial-examples.md)
