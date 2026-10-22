# asyncio — Concurrency and Multithreading

### Concurrency and Multithreading

An event loop lives on one thread — usually the main one — and carries out every callback and Task right there on that thread. As long as one Task occupies the event loop, no other Task on that same thread can proceed. The moment a Task hits an `await` expression, that Task is paused and the event loop moves on to the next one.

When you want to schedule a [callback](https://docs.python.org/3.14/glossary.html#term-callback) from a separate OS thread, reach for the [`loop.call_soon_threadsafe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe) method. Example:

```python
loop.call_soon_threadsafe(callback, *args)

```

The vast majority of asyncio objects lack thread safety, which usually causes no trouble so long as nothing touches them from beyond a Task or a callback. Where such outside code does have to invoke a low-level asyncio API, lean on the [`loop.call_soon_threadsafe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe) method, for example:

```python
loop.call_soon_threadsafe(fut.cancel)

```

For scheduling a coroutine object out of another OS thread, turn to the [`run_coroutine_threadsafe()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.run_coroutine_threadsafe) function. What it hands back is a [`concurrent.futures.Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future) through which you can reach the result:

```python
async def coro_func():
     return await asyncio.sleep(1, 42)

# Later in another OS thread:

future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
# Wait for the result:
result = future.result()

```

For signals to be handled, the event loop has to run on the main thread.

Pairing the [`loop.run_in_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) method with a [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) or an [`InterpreterPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor) lets you run blocking code over on a separate OS thread, leaving the OS thread that hosts the event loop unblocked.

As things stand, there’s no facility to schedule coroutines or callbacks straight from another process — say one launched via [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing). Under [Event loop methods](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-event-loop-methods) you’ll find APIs that read from pipes and keep an eye on file descriptors without stalling the event loop. Beyond that, asyncio’s [Subprocess](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio-subprocess) APIs offer a route to spin up a process and talk to it from the event loop. Finally, the same [`loop.run_in_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) method noted above pairs with a [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) as well, running your code in a separate process.

[Subject index](INDEX.md) · [Previous](debug-mode.md) · [Continue](running-blocking-code.md)
