# multiprocessing / Synchronization primitives: `multiprocessing.RLock`, `acquire()`, `release()`, `locked()`

*class *multiprocessing.RLock

A recursive lock object: a close analog of [`threading.RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock). The process or thread that took a recursive lock is the one that has to release it. After a process or thread takes a recursive lock, that same process or thread may take it again without blocking; that process or thread then has to release it as many times as it took it.

Be aware that `RLock` is in fact a factory function handing back an instance of `multiprocessing.synchronize.RLock` set up with a default context.

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

`RLock` supports the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol and thus may be used in [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements.

 acquire(*block=True*, *timeout=None*)

Take a lock, in either a blocking or a non-blocking way.

Called with the *block* argument set to `True`, block until the lock sits unlocked (owned by no process or thread) unless the current process or thread already owns it. The current process or thread then assumes ownership of the lock (when it does not already hold it) and the recursion level inside the lock rises by one, giving back `True`. Note that this first argument's behavior carries several differences from the implementation of [`threading.RLock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.RLock.acquire), the argument's own name among them.

Called with the *block* argument set to `False`, do not block. When the lock has already been taken (and is thus owned) by some other process or thread, the current process or thread does not assume ownership and the recursion level inside the lock stays put, giving back `False`. When the lock sits unlocked, the current process or thread assumes ownership and the recursion level rises, giving back `True`.

The *timeout* argument's use and behaviors match those in `Lock.acquire()`. Note that a few of these *timeout* behaviors differ from the implemented behaviors in [`threading.RLock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.RLock.acquire).

 release()

Release a lock, dropping the recursion level by one. When that decrement leaves the recursion level at zero, reset the lock to unlocked (owned by no process or thread), and when other processes or threads are blocked waiting for the lock to open up, let exactly one of them go ahead. When that decrement leaves the recursion level still above zero, the lock keeps being locked and owned by the calling process or thread.

Call this method only when the calling process or thread holds the lock. An [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) is raised when this method gets called by a process or thread that is not the owner, or when the lock sits unlocked (unowned). Note that the kind of exception raised here differs from the implemented behavior in [`threading.RLock.release()`](https://docs.python.org/3.14/library/threading.html#threading.RLock.release).

 locked()

Give back a boolean telling whether this object is locked at the moment.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](multiprocessing-lock-class-to-multiprocessing-lock-locked.md) · [Continue](process-semaphore-contract.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Synchronization primitives](multiprocessing-barrier-class.md)
