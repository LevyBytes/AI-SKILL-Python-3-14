# Lock: `asyncio.Lock`

### Lock

 *class *asyncio.Lock

Provides a mutex lock for asyncio tasks. Carries no thread safety.

You can rely on an asyncio lock to secure exclusive access to a resource that is shared.

The recommended approach for working with a Lock is an [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statement:

```python
lock = asyncio.Lock()

# ... later
async with lock:
    # access shared state

```

which is equivalent to:

```python
lock = asyncio.Lock()

# ... later
await lock.acquire()
try:
    # access shared state
finally:
    lock.release()

```

Changed in version 3.10: Removed the *loop* parameter.

[Subject index](INDEX.md) · [Previous](synchronization-primitives.md) · [Continue](asyncio-lock-acquire-to-asyncio-lock-locked.md)
