# A homemade asyncio.sleep

### A homemade asyncio.sleep

We will walk through an example showing how a future could be put to use to build your own flavor of asynchronous sleep (`async_sleep`) that imitates [`asyncio.sleep()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.sleep).

This snippet hands a few tasks to the event loop and then awaits the task produced by `asyncio.create_task`, which encloses the `async_sleep(3)` coroutine. The goal is for that task to complete only after three seconds have passed, yet without keeping other tasks from running.

```python
async def other_work():
    print("I like work. Work work.")

async def main():
    # Add a few other tasks to the event loop, so there's something
    # to do while asynchronously sleeping.
    work_tasks = [
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work())
    ]
    print(
        "Beginning asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    await asyncio.create_task(async_sleep(3))
    print(
        "Done asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    # asyncio.gather effectively awaits each task in the collection.
    await asyncio.gather(*work_tasks)

```

Below, a future gives us custom control over the moment that task gets marked as done. Should [`future.set_result()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.set_result) (the method that marks a future as done) never get called, then the task will never complete. We have also brought in another task, which you will see shortly, that keeps track of how much time has gone by and, when appropriate, calls `future.set_result()`.

```python
async def async_sleep(seconds: float):
    future = asyncio.Future()
    time_to_wake = time.time() + seconds
    # Add the watcher-task to the event loop.
    watcher_task = asyncio.create_task(_sleep_watcher(future, time_to_wake))
    # Block until the future is marked as done.
    await future

```

Below, we rely on a rather minimal `YieldToEventLoop()` object to `yield` from its `__await__` method, surrendering control to the event loop. This amounts to the same thing as calling `asyncio.sleep(0)`, yet this route is clearer, and besides, leaning on `asyncio.sleep` while demonstrating how to build it would be a bit of a cheat! As it usually does, the event loop runs through its tasks, granting them control and getting control back when they pause or complete. The `watcher_task`, running the coroutine `_sleep_watcher(...)`, gets called once during each complete cycle of the event loop. At every resumption it checks the time, and if not enough has gone by, it pauses again and returns control to the event loop. After enough time has gone by, `_sleep_watcher(...)` marks the future done and finishes by leaving its endless `while` loop. Because this helper task runs only once per event loop cycle, you would be right to point out that this asynchronous sleep sleeps *at least* three seconds rather than precisely three seconds. The same holds for `asyncio.sleep` as well.

```python
class YieldToEventLoop:
    def __await__(self):
        yield

async def _sleep_watcher(future, time_to_wake):
    while True:
        if time.time() >= time_to_wake:
            # This marks the future as done.
            future.set_result(None)
            break
        else:
            await YieldToEventLoop()

```

Here is the full program's output:

```none
$ python custom-async-sleep.py
Beginning asynchronous sleep at time: 14:52:22.
I like work. Work work.
I like work. Work work.
I like work. Work work.
Done asynchronous sleep at time: 14:52:25.

```

It might seem to you that this take on asynchronous sleep was needlessly convoluted. And, honestly, it was. The intent of the example was to demonstrate how versatile futures are using a straightforward case that you could copy for trickier requirements. For comparison, you could build it without any futures, like this:

```python
async def simpler_async_sleep(seconds):
    time_to_wake = time.time() + seconds
    while True:
        if time.time() >= time_to_wake:
            return
        else:
            await YieldToEventLoop()

```

But that is everything for the time being. Hopefully you now feel ready to dive into a bit of async programming with more confidence or explore advanced topics in the [`rest of the documentation`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio).

[Subject index](INDEX.md) · [Previous source context](futures.md)
