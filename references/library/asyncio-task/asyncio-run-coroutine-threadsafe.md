# Scheduling from other threads

### Scheduling from other threads

 asyncio.run_coroutine_threadsafe(*coro*, *loop*)

Submit a coroutine to the given event loop. Thread-safe.

Return a [`concurrent.futures.Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future) to wait for the result from another OS thread.

You are expected to invoke this function from an OS thread other than the one hosting the event loop. Example:

```python
def in_thread(loop: asyncio.AbstractEventLoop) -> None:
    # Run some blocking IO
    pathlib.Path("example.txt").write_text("hello world", encoding="utf8")

    # Create a coroutine
    coro = asyncio.sleep(1, result=3)

    # Submit the coroutine to a given loop
    future = asyncio.run_coroutine_threadsafe(coro, loop)

    # Wait for the result with an optional timeout argument
    assert future.result(timeout=2) == 3

async def amain() -> None:
    # Get the running loop
    loop = asyncio.get_running_loop()

    # Run something in a thread
    await asyncio.to_thread(in_thread, loop)

```

The reverse arrangement works too. Example:

```python
@contextlib.contextmanager
def loop_in_thread() -> Generator[asyncio.AbstractEventLoop]:
    loop_fut = concurrent.futures.Future[asyncio.AbstractEventLoop]()
    stop_event = asyncio.Event()

    async def main() -> None:
        loop_fut.set_result(asyncio.get_running_loop())
        await stop_event.wait()

    with concurrent.futures.ThreadPoolExecutor(1) as tpe:
        complete_fut = tpe.submit(asyncio.run, main())
        for fut in concurrent.futures.as_completed((loop_fut, complete_fut)):
            if fut is loop_fut:
                loop = loop_fut.result()
                try:
                    yield loop
                finally:
                    loop.call_soon_threadsafe(stop_event.set)
            else:
                fut.result()

# Create a loop in another thread
with loop_in_thread() as loop:
    # Create a coroutine
    coro = asyncio.sleep(1, result=3)

    # Submit the coroutine to a given loop
    future = asyncio.run_coroutine_threadsafe(coro, loop)

    # Wait for the result with an optional timeout argument
    assert future.result(timeout=2) == 3

```

When the coroutine raises an exception, that gets reported on the returned Future. The Future is also a way to cancel the task running inside the event loop:

```python
try:
    result = future.result(timeout)
except TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')

```

Consult the [concurrency and multithreading](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-multithreading) part of the docs.

In contrast to the other asyncio functions, this one demands that you pass the *loop* argument explicitly.

Added in version 3.5.1.

[Subject index](INDEX.md) · [Continue](asyncio-current-task-to-asyncio-iscoroutine.md)
