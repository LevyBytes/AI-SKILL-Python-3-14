# Condition: `asyncio.Condition`

### Condition

 *class *asyncio.Condition(*lock=None*)

A Condition object. Carries no thread safety.

A task can employ an asyncio condition primitive to await some occurrence and afterward claim exclusive access to a shared resource.

At its core, a Condition object rolls together what an `Event` and a `Lock` each do. Several Condition objects may share a single Lock, which lets you coordinate exclusive access to a shared resource among various tasks that each care about specific states of that resource.

The optional *lock* argument has to be either a `Lock` object or `None`. In the `None` case, a fresh Lock object is generated for you.

Changed in version 3.10: Removed the *loop* parameter.

The recommended approach for working with a Condition is an [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statement:

```python
cond = asyncio.Condition()

# ... later
async with cond:
    await cond.wait()

```

which is equivalent to:

```python
cond = asyncio.Condition()

# ... later
await cond.acquire()
try:
    await cond.wait()
finally:
    cond.release()

```

[Subject index](INDEX.md) · [Previous](asyncio-event-wait-to-asyncio-event-is-set.md) · [Continue](asyncio-condition-acquire-to-asyncio-condition-wait-for.md)
