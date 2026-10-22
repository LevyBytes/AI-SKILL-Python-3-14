# Thread-local storage support

## Thread-local storage support

### Thread-local storage support

CPython's interpreter offers low-level facilities for thread-local storage (TLS); these wrap the platform's native TLS so that the Python-level thread-local storage API ([`threading.local`](https://docs.python.org/3.14/library/threading.html#threading.local)) is supported. At the C level, CPython's APIs resemble what pthreads and Windows expose: you employ a thread key plus functions that bind a per-thread void* value.

You do *not* need an [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) to call these functions; each one performs its own locking.

Be aware that the TLS API declarations are absent from `Python.h`; including `pythread.h` is necessary before you can use thread-local storage.

Note

These API functions perform no memory management for the void* values on your behalf. Allocating and freeing them is your responsibility. And if those void* values turn out to be [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, the functions perform no refcount operations on them either.

[Subject index](INDEX.md) · [Previous source contract](../pytime-c-api/pytime-assecondsdouble.md) · [Following source contract](thread-specific-storage-api.md)
