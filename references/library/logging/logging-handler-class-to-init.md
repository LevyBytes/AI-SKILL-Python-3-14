# logging / Handler Objects: `logging.Handler`, `__init__()`

### Handler Objects

These attributes and methods belong to Handlers. Be aware that `Handler` is never instantiated directly; the class serves as a base for more useful subclasses. That said, the `__init__()` method in subclasses needs to call `Handler.__init__()`.

 *class *logging.Handler

 __init__(*level=NOTSET*)

Initializes the `Handler` instance: it sets the level, empties out the list of filters, and builds a lock (via `createLock()`) that serializes access to an I/O mechanism.

[Subject index](INDEX.md) · [Previous](logging-levels.md) · [Continue](logging-handler-createlock-to-logging-handler-emit.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
