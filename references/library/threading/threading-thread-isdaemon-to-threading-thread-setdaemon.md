# threading.Thread: `isDaemon()`, `setDaemon()`

A boolean flag that reports whether the thread runs as a daemon thread (`True`) or otherwise (`False`). You have to assign it prior to calling `start()`; doing so afterward triggers a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). The starting value comes from the thread that spawned it; since the main thread is never a daemon, every thread spawned from the main thread starts out with `daemon` = `False`.

Once there remain no living non-daemon threads, the whole Python program terminates.

 isDaemon()

 setDaemon()

A deprecated getter/setter pair for `daemon`; reach for the property directly instead.

Deprecated since version 3.10.

[Subject index](INDEX.md) · [Continue](threading-lock-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.Thread](threading-thread-class.md) · [Owning module, declaration or section: Thread objects](threading-thread-class.md) · [Owning module, declaration or section: daemon](threading-thread-is-alive.md) · [Preceding source contract and version conditions](threading-thread-is-alive.md)
