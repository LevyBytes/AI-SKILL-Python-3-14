# threading.Semaphore: `acquire()`, `release()`

acquire(*blocking=True*, *timeout=None*)

Take a semaphore.

When called with no arguments:

- Should the internal counter be above zero on entry, lower it by one and hand back `True` right away.

- Should the internal counter be zero on entry, block until a `release()` call wakes it. Once woken (and the counter is above 0), lower the counter by 1 and hand back `True`. Each `release()` call wakes precisely one thread. You should not depend on the order in which threads wake.

When called with *blocking* equal to `False`, never wait. Should a call with no argument have blocked, hand back `False` right away; otherwise behave as in the no-argument case and hand back `True`.

When called with a *timeout* other than `None`, it blocks no longer than *timeout* seconds. Should acquire not finish successfully within that span, hand back `False`. Otherwise hand back `True`.

Changed in version 3.2: The *timeout* parameter is new.

 release(*n=1*)

Free a semaphore, raising the internal counter by *n*. When it stood at zero on entry and other threads are waiting for it to climb above zero again, wake *n* of those threads.

Changed in version 3.9: The *n* parameter was added so that several waiting threads can be released together.

[Subject index](INDEX.md) · [Previous](threading-semaphore-class.md) · [Continue](threading-boundedsemaphore-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.Semaphore](threading-semaphore-class.md) · [Owning module, declaration or section: Semaphore objects](threading-semaphore-class.md)
