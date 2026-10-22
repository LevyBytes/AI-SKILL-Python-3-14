# Semaphore: `acquire()`, `locked()`, `release()`

*async *acquire()

Take hold of a semaphore.

When the internal counter stands above zero, lower it by one and give back `True` straight away. When it is zero, hold off until a `release()` happens and then give back `True`.

 locked()

Gives back `True` whenever the semaphore cannot be taken right away.

 release()

Let go of a semaphore, raising the internal counter by one. This can rouse a task that is waiting to take the semaphore.

In contrast to `BoundedSemaphore`, a `Semaphore` permits issuing more `release()` calls than `acquire()` calls.

[Subject index](INDEX.md) · [Previous](asyncio-semaphore-class.md) · [Continue](asyncio-boundedsemaphore-class.md) · [Owning module, declaration or section: asyncio.Semaphore](asyncio-semaphore-class.md) · [Owning module, declaration or section: Semaphore](asyncio-semaphore-class.md)
