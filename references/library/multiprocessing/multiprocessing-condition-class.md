# multiprocessing: `multiprocessing.Condition`

*class *multiprocessing.Condition([*lock*])

A condition variable: an alias for [`threading.Condition`](https://docs.python.org/3.14/library/threading.html#threading.Condition).

Should *lock* be supplied, it ought to be a `Lock` or `RLock` object out of `multiprocessing`.

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

Changed in version 3.3: The [`wait_for()`](https://docs.python.org/3.14/library/threading.html#threading.Condition.wait_for) method was added.

[Subject index](INDEX.md) · [Previous](bounded-process-semaphore.md) · [Continue](multiprocessing-event-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Synchronization primitives](multiprocessing-barrier-class.md)
