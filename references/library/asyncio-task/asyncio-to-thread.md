# Running in threads

### Running in threads

 *async *asyncio.to_thread(*func*, */*, **args*, ***kwargs*)

Asynchronously run function *func* in a separate thread.

Whatever *args and **kwargs you give this function pass straight through to *func*. On top of that, the active [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) carries over, so context variables from the event loop thread remain reachable inside the separate thread.

Hand back a coroutine you can await to eventually obtain *func*’s result.

The main purpose of this coroutine function is running IO-bound functions or methods that would otherwise stall the event loop if executed on the main thread. For example:

```python
def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")

asyncio.run(main())

# Expected output:
#
# started main at 19:50:53
# start blocking_io at 19:50:53
# blocking_io complete at 19:50:54
# finished main at 19:50:54

```

Were you to call `blocking_io()` straight from a coroutine, the event loop would stall for as long as it ran, adding 1 second to the total runtime. With `asyncio.to_thread()` instead, the call executes on its own thread and the event loop keeps going.

Note

Because of the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL), `asyncio.to_thread()` is generally limited to making IO-bound functions non-blocking. That said, extension modules that release the GIL, or Python implementations that lack one altogether, let `asyncio.to_thread()` serve CPU-bound functions as well.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](asyncio-as-completed.md) · [Continue](asyncio-run-coroutine-threadsafe.md)
