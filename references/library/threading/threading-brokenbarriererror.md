# threading.BrokenBarrierError and context-managed synchronization

*exception *threading.BrokenBarrierError

Derived from [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError), this error gets thrown whenever a `Barrier` object enters a broken state or undergoes a reset.

### Using locks, conditions, and semaphores in the `with` statement

Every object this module exposes that carries `acquire` and `release` methods works as a context manager inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Entering the block triggers a call to `acquire`, while leaving it triggers `release`. So this fragment below:

```python
with some_lock:
    # do something...

```

is equivalent to:

```python
some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()

```

At present, the `Lock`, `RLock`, `Condition`, `Semaphore`, and `BoundedSemaphore` objects each qualify for use as context managers within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

[Subject index](INDEX.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: Barrier objects](threading-barrier-class.md)
