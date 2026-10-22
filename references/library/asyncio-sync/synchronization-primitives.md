# Synchronization Primitives

# Asyncio Sync

### Synchronization Primitives

**Source code:** [Lib/asyncio/locks.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/locks.py)

---

The synchronization primitives in asyncio are built to resemble those found in the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module, subject to two significant qualifications:

- these asyncio primitives carry no thread safety, so they ought not serve for OS thread synchronization (reach for [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) in that situation);

- the methods on these synchronization primitives take no *timeout* argument; when you need operations bounded by a timeout, apply the [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) function instead.

The basic synchronization primitives that asyncio offers are these:

- `Lock`

- `Event`

- `Condition`

- `Semaphore`

- `BoundedSemaphore`

- `Barrier`

---

[Subject index](INDEX.md) · [Continue](asyncio-lock-class.md)
