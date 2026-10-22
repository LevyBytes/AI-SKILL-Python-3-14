# threading — `Semaphore` example

### `Semaphore` example

Semaphores often serve to guard resources of limited capacity, a database server being one example. Whenever the resource's size is fixed, reach for a bounded semaphore. Ahead of launching any worker threads, your main thread would set up the semaphore:

```python
maxconnections = 5
# ...
pool_sema = BoundedSemaphore(value=maxconnections)

```

After being launched, worker threads invoke the semaphore's acquire and release methods whenever they have to connect to the server:

```python
with pool_sema:
    conn = connectdb()
    try:
        # ... use connection ...
    finally:
        conn.close()

```

Relying on a bounded semaphore lowers the odds that a coding mistake which frees the semaphore more often than it takes it will slip by unnoticed.

[Subject index](INDEX.md) · [Previous](threading-boundedsemaphore-class.md) · [Continue](threading-event-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
