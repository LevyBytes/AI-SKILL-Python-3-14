# Shielding from cancellation

### Shielding from cancellation

 *awaitable *asyncio.shield(*aw*)

Protect an awaitable object from being `cancelled`.

If *aw* is a coroutine it is automatically scheduled as a Task.

The statement:

```python
task = asyncio.create_task(something())
res = await shield(task)

```

is equivalent to:

```python
res = await something()

```

*except* this: should the coroutine that contains it get cancelled, the Task running within `something()` stays uncancelled. As far as `something()` can tell, no cancellation occurred. Even so, its caller does still get cancelled, so the “await” expression nonetheless raises a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError).

Were `something()` to be cancelled by some other route (that is, from inside itself), that would cancel `shield()` too.

Where you'd like to disregard cancellation altogether (which is discouraged), pair the `shield()` function with a try/except clause in the following manner:

```python
task = asyncio.create_task(something())
try:
    res = await shield(task)
except CancelledError:
    res = None

```

Important

Hold onto a reference to tasks you pass into this function, so that a task doesn't vanish partway through running. Tasks are tracked by the event loop with weak references only. Any task not referenced from somewhere else is liable to be garbage collected at any moment, possibly before finishing.

Changed in version 3.10: Removed the *loop* parameter.

Deprecated since version 3.10: A deprecation warning gets raised when *aw* is not a Future-like object while no event loop is currently running.

[Subject index](INDEX.md) · [Previous](eager-task-factory-creation.md) · [Continue](asyncio-timeout.md)
