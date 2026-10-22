# threading: `threading.Lock`

### Lock objects

A primitive lock acts as a synchronization primitive that, while held, belongs to no specific thread. Within Python it stands as the most basic synchronization primitive on offer today, built straight into the [`_thread`](https://docs.python.org/3.14/library/_thread.html#module-_thread) extension module.

At any moment a primitive lock sits in either the “locked” or the “unlocked” state, starting life unlocked. Two core methods govern it: `acquire()` and `release()`. While the lock is unlocked, `acquire()` flips it to locked and comes back right away. While it is locked, `acquire()` waits until some other thread's `release()` flips it back to unlocked, after which the `acquire()` call locks it again and returns. You should invoke `release()` only on a locked lock; it flips the state to unlocked and returns straight away. Trying to release a lock that is already unlocked produces a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Locks honor the context management protocol as well.

If several threads sit blocked inside `acquire()` awaiting the unlocked state, just one of them moves forward when a `release()` call flips the state back to unlocked; exactly which waiting thread advances is left undefined and can differ between implementations.

Every method runs atomically.

 *class *threading.Lock

The class that provides primitive lock objects. After one thread takes a lock, any further attempts to take it will block until it is freed; releasing it may be done by any thread.

Changed in version 3.13: `Lock` is now a class. With older Pythons, `Lock` was a factory function that handed back an instance of the hidden underlying lock type.

[Subject index](INDEX.md) · [Previous](threading-thread-isdaemon-to-threading-thread-setdaemon.md) · [Continue](threading-lock-acquire-to-threading-lock-locked.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
