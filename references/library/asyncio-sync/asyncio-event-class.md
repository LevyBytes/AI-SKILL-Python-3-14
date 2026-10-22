# Event: `asyncio.Event`

### Event

 *class *asyncio.Event

An event object. Carries no thread safety.

An asyncio event serves to signal a number of asyncio tasks that something has taken place.

Internally an Event object keeps a flag that the `set()` method turns *true* and the `clear()` method puts back to *false*. The `wait()` method holds until that flag becomes *true*. At the start the flag holds *false*.

Changed in version 3.10: Removed the *loop* parameter.

Example:

```python
async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main():
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()

    # Wait until the waiter task is finished.
    await waiter_task

asyncio.run(main())

```

[Subject index](INDEX.md) · [Previous](asyncio-lock-acquire-to-asyncio-lock-locked.md) · [Continue](asyncio-event-wait-to-asyncio-event-is-set.md)
