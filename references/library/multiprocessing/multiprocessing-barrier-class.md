# multiprocessing: `multiprocessing.Barrier`

### Synchronization primitives

By and large, synchronization primitives are less essential in a multiprocess program than in a multithreaded one. Consult the documentation for the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module.

Be aware that synchronization primitives can also be created from a manager object — see Managers.

 *class *multiprocessing.Barrier(*parties*[, *action*[, *timeout*]])

A barrier object: a clone of [`threading.Barrier`](https://docs.python.org/3.14/library/threading.html#threading.Barrier).

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](connection-byte-receive-methods.md) · [Continue](bounded-process-semaphore.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
