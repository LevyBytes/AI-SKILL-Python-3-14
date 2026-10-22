# threading: `threading.RLock`

### RLock objects

A reentrant lock is a synchronization primitive that the same thread can take more than once. Under the hood it relies on the notions of “owning thread” and “recursion level” on top of the locked/unlocked state that primitive locks use. While locked, a particular thread owns the lock; while unlocked, ownership belongs to no thread.

To lock it, threads invoke the lock's `acquire()` method, and to unlock it they invoke its `release()` method.

Note

Because reentrant locks honor the context management protocol, using [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) is the recommended way to take and free the lock around a block of code, rather than calling `acquire()` and `release()` by hand.

An RLock allows nested `acquire()`/`release()` call pairs, which Lock's `acquire()`/`release()` do not. Only the closing `release()` (the `release()` belonging to the outermost pair) returns the lock to an unlocked state and frees up another thread that is blocked inside `acquire()` to advance.

You must employ `acquire()`/`release()` in matched pairs: each acquire needs a matching release within the thread that took the lock. Neglecting to release as many times as the lock was acquired can produce deadlock.

 *class *threading.RLock

This class provides reentrant lock objects. Whichever thread took a reentrant lock is the one that has to free it. After a thread has taken a reentrant lock, that same thread can take it again without blocking; it then has to release it once per acquisition.

Be aware that `RLock` is really a factory function that hands back an instance of the most efficient build of the concrete RLock class the platform supports.

[Subject index](INDEX.md) · [Previous](threading-lock-acquire-to-threading-lock-locked.md) · [Continue](threading-rlock-acquire-to-threading-rlock-locked.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
