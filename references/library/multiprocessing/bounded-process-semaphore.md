# multiprocessing / Synchronization primitives: `multiprocessing.BoundedSemaphore`, `locked()`

*class *multiprocessing.BoundedSemaphore([*value*])

A bounded semaphore object: a close analog of [`threading.BoundedSemaphore`](https://docs.python.org/3.14/library/threading.html#threading.BoundedSemaphore).

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

There is exactly one way it diverges from its close analog: the first argument of its `acquire` method is called *block*, matching `Lock.acquire()`.

 locked()

Give back a boolean telling whether this object is locked at the moment.

Added in version 3.14.

Note

On macOS, this cannot be told apart from `Semaphore`, because `sem_getvalue()` is not implemented on that platform.

[Subject index](INDEX.md) · [Previous](multiprocessing-barrier-class.md) · [Continue](multiprocessing-condition-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Synchronization primitives](multiprocessing-barrier-class.md)
