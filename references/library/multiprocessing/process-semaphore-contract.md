# multiprocessing / Synchronization primitives: `multiprocessing.Semaphore`, `get_value()`, `locked()`

*class *multiprocessing.Semaphore([*value*])

A semaphore object: a close analog of [`threading.Semaphore`](https://docs.python.org/3.14/library/threading.html#threading.Semaphore).

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

There is exactly one way it diverges from its close analog: the first argument of its `acquire` method is called *block*, matching `Lock.acquire()`.

 get_value()

Give back the semaphore's current value.

Be aware this may raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) on platforms such as macOS where `sem_getvalue()` is unavailable.

 locked()

Give back a boolean telling whether this object is locked at the moment.

Added in version 3.14.

Note

On macOS, `sem_timedwait` has no support, so passing a timeout to `acquire()` mimics that function's behavior through a sleeping loop.

Note

Part of this package's functionality relies on a working shared semaphore implementation in the host operating system. Lacking one, the `multiprocessing.synchronize` module is switched off, and any attempt to import it raises an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError). For more information see [bpo-3770](https://bugs.python.org/issue?@action=redirect&bpo=3770).

[Subject index](INDEX.md) · [Previous](multiprocessing-rlock-class-to-multiprocessing-rlock-locked.md) · [Continue](multiprocessing-value-to-multiprocessing-array.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Synchronization primitives](multiprocessing-barrier-class.md)
