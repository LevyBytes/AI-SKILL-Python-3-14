# multiprocessing / Synchronization primitives: `multiprocessing.Lock`, `acquire()`, `release()`, `locked()`

*class *multiprocessing.Lock

A non-recursive lock object: a close analog of [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock). After a process or thread takes a lock, any later attempt to take it from any process or thread blocks until the lock is released; any process or thread is free to release it. The notions and behaviors that `threading.Lock` carries for threads carry over here into `multiprocessing.Lock` for either processes or threads, save where stated otherwise.

Be aware that `Lock` is in fact a factory function handing back an instance of `multiprocessing.synchronize.Lock` set up with a default context.

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

`Lock` supports the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol and thus may be used in [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements.

 acquire(*block=True*, *timeout=None*)

Take a lock, in either a blocking or a non-blocking way.

With the *block* argument left at `True` (the default), the call blocks until the lock sits unlocked, then flips it to locked and gives back `True`. Note that this first argument carries a different name from the one in [`threading.Lock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire).

With the *block* argument set to `False`, the call does not block. When the lock currently sits locked, give back `False`; otherwise flip the lock to a locked state and give back `True`.

Called with a positive floating-point *timeout*, it blocks for no more than that many seconds while the lock stays unattainable. Calls passing a negative *timeout* behave the same as a *timeout* of zero. Calls passing a *timeout* of `None` (the default) make the timeout span infinite. Note that how negative or `None` *timeout* values get handled differs from the implemented behavior in [`threading.Lock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire). The *timeout* argument bears no practical weight once *block* is `False`, so it is ignored then. Gives back `True` once the lock is taken, or `False` if the timeout span ran out.

 release()

Release a lock. Any process or thread can do this, not solely the process or thread that first took the lock.

The behavior matches [`threading.Lock.release()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.release), except that calling it on an unlocked lock raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 locked()

Give back a boolean telling whether this object is locked at the moment.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](multiprocessing-event-class.md) · [Continue](multiprocessing-rlock-class-to-multiprocessing-rlock-locked.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Synchronization primitives](multiprocessing-barrier-class.md)
