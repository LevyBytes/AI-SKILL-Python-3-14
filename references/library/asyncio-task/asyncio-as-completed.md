# asyncio.task: `asyncio.as_completed()`

asyncio.as_completed(*aws*, ***, *timeout=None*)

Run the awaitable objects from the *aws* iterable side by side. Iterating the object it hands back lets you collect each awaitable’s result as that awaitable completes.

You can walk over the object that `as_completed()` returns either as an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) or as an ordinary [iterator](https://docs.python.org/3.14/glossary.html#term-iterator). With asynchronous iteration, any awaitables that were originally supplied are yielded back when they are tasks or futures. That makes lining up earlier-scheduled tasks against their outcomes straightforward. Example:

```python
ipv4_connect = create_task(open_connection("127.0.0.1", 80))
ipv6_connect = create_task(open_connection("::1", 80))
tasks = [ipv4_connect, ipv6_connect]

async for earliest_connect in as_completed(tasks):
    # earliest_connect is done. The result can be obtained by
    # awaiting it or calling earliest_connect.result()
    reader, writer = await earliest_connect

    if earliest_connect is ipv6_connect:
        print("IPv6 connection established.")
    else:
        print("IPv4 connection established.")

```

While iterating asynchronously, tasks created behind the scenes are yielded for any supplied awaitables that are neither tasks nor futures.

As an ordinary iterator, every pass yields a fresh coroutine that returns the result or raises the exception of the next awaitable to complete. The approach works with Python releases that predate 3.13:

```python
ipv4_connect = create_task(open_connection("127.0.0.1", 80))
ipv6_connect = create_task(open_connection("::1", 80))
tasks = [ipv4_connect, ipv6_connect]

for next_connect in as_completed(tasks):
    # next_connect is not one of the original task objects. It must be
    # awaited to obtain the result value or raise the exception of the
    # awaitable that finishes next.
    reader, writer = await next_connect

```

If the timeout elapses before every awaitable has completed, a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) is raised. During asynchronous iteration the `async for` loop raises it, and during plain iteration the yielded coroutines do.

Changed in version 3.10: Removed the *loop* parameter.

Deprecated since version 3.10: A deprecation warning fires when some awaitable object inside the *aws* iterable is not Future-like and no event loop is currently running.

Changed in version 3.12: Added support for generators yielding tasks.

Changed in version 3.13: You may now treat the result either as an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) or as a plain [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) (formerly it served only as a plain iterator).

[Subject index](INDEX.md) · [Previous](asyncio-wait.md) · [Continue](asyncio-to-thread.md) · [Owning module, declaration or section: Waiting primitives](asyncio-wait.md)
