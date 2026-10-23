# signal - Signals and threads

### Signals and threads

No matter which thread the signal actually arrived in, Python signal handlers run exclusively in the main Python thread belonging to the main interpreter. Consequently, you cannot rely on signals to pass messages between threads. Reach for the synchronization primitives in the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module for that purpose instead.

On top of that, the privilege of registering a new signal handler belongs solely to the main thread of the main interpreter.

Warning

Avoid using synchronization primitives such as [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) inside signal handlers. That practice can produce surprising deadlocks.

[Subject index](INDEX.md) · [Previous](execution-of-python-signal-handlers.md) · [Continue](signal-signals-class.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md)
