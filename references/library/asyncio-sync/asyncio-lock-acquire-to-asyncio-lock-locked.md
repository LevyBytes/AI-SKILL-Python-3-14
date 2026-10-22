# Lock: `acquire()`, `release()`, `locked()`

*async *acquire()

Take hold of the lock.

This method holds off until the lock sits *unlocked*, flips it to *locked*, and hands back `True`.

If several coroutines are stuck inside `acquire()` awaiting the lock's release, just one of them eventually moves forward.

Lock acquisition is *fair*: the coroutine allowed to continue is whichever one began waiting on the lock earliest.

 release()

Let go of the lock.

While the lock stands *locked*, switch it back to *unlocked* and return.

Should the lock already be *unlocked*, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) gets raised.

 locked()

Hand back `True` whenever the lock is *locked*.

[Subject index](INDEX.md) · [Previous](asyncio-lock-class.md) · [Continue](asyncio-event-class.md) · [Owning module, declaration or section: asyncio.Lock](asyncio-lock-class.md) · [Owning module, declaration or section: Lock](asyncio-lock-class.md)
