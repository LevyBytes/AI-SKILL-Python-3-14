# Awaitables

### Awaitables

An object qualifies as an **awaitable** object when it is usable within an [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expression. A great many asyncio APIs are built to take awaitables.

Three principal kinds of *awaitable* objects exist: **coroutines**, **Tasks**, and **Futures**.

Coroutines

Since Python coroutines are *awaitables*, one coroutine may await another:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()  # will raise a "RuntimeWarning".

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())

```

Important

Throughout this documentation, the word “coroutine” may stand for either of two tightly linked ideas:

- a *coroutine function*: an [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) function;

- a *coroutine object*: the object you get back from invoking a *coroutine function*.

Tasks

The role of *Tasks* is to schedule coroutines for *concurrent* execution.

Whenever a coroutine gets wrapped into a *Task* through functions such as `asyncio.create_task()`, that coroutine is queued to run shortly thereafter:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())

```

Futures

A [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) is a particular **low-level** awaitable object standing for the **eventual result** that an asynchronous operation will yield.

Awaiting a Future object signifies that the coroutine pauses until that Future gets resolved somewhere else.

The purpose of Future objects within asyncio is to make callback-based code interoperable with async/await.

Typically **there is no need** for application-level code to construct Future objects directly.

Some libraries and certain asyncio APIs hand back Future objects, which you can then await:

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )

```

One solid illustration of a low-level routine that hands back a Future object is [`loop.run_in_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_in_executor).

[Subject index](INDEX.md) · [Previous](../coroutines/code-example-async-def-main.md) · [Continue](asyncio-create-task.md)
