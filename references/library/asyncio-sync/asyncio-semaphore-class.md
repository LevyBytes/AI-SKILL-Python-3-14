# Semaphore: `asyncio.Semaphore`

### Semaphore

 *class *asyncio.Semaphore(*value=1*)

A Semaphore object. Carries no thread safety.

A semaphore keeps an internal counter that every `acquire()` call lowers by one and every `release()` call raises by one. That counter is not allowed to drop below zero; when `acquire()` sees it at zero, it blocks and waits for some task to invoke `release()`.

The optional *value* argument supplies the starting figure for the internal counter (`1` unless given otherwise). Supplying a value under `0` raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Changed in version 3.10: Removed the *loop* parameter.

The recommended approach for working with a Semaphore is an [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statement:

```python
sem = asyncio.Semaphore(10)

# ... later
async with sem:
    # work with shared resource

```

which is equivalent to:

```python
sem = asyncio.Semaphore(10)

# ... later
await sem.acquire()
try:
    # work with shared resource
finally:
    sem.release()

```

[Subject index](INDEX.md) · [Previous](asyncio-condition-acquire-to-asyncio-condition-wait-for.md) · [Continue](asyncio-semaphore-acquire-to-asyncio-semaphore-release.md)
