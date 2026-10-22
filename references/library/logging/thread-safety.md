# logging — Thread Safety

### Thread Safety

The logging module is meant to be thread-safe with no special work required of its clients. It reaches this through the use of threading locks; one lock serializes access to the module's shared data, and each handler additionally creates a lock that serializes access to its underlying I/O.

If you are building asynchronous signal handlers with the [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module, you may find yourself unable to use logging from inside such handlers. The reason is that lock implementations within the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module are not always re-entrant, and so cannot be called from such signal handlers.

[Subject index](INDEX.md) · [Previous](logging-loggeradapter-process.md) · [Continue](logging-getlogger-to-logging-exception.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
