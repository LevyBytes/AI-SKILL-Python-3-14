# Safe on shared objects

### Safe on shared objects

Such a function or operation is fine for simultaneous use against the **same** object. Internal synchronization in the implementation (for instance [per-object locks](https://docs.python.org/3.14/glossary.html#term-per-object-lock) or [critical sections](https://docs.python.org/3.14/c-api/synchronization.html#python-critical-section-api)) guards the shared mutable state, which means callers need not add locking of their own.

Example: [`PyList_GetItemRef()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItemRef) is callable across several threads on one shared [`PyListObject`](https://docs.python.org/3.14/c-api/list.html#c.PyListObject) - internal synchronization serializes the access for it.

[Subject index](INDEX.md) · [Previous](safe-on-distinct-objects.md) · [Continue](atomic.md)
