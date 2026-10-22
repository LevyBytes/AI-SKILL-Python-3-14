# thread local storage support C API: Thread-specific storage purpose and lifecycle

### Thread-specific storage API

The thread-specific storage (TSS) API arrived to replace the older TLS API used inside the CPython interpreter. Rather than int, this API adopts a fresh type, `Py_tss_t`, for representing thread keys.

Added in version 3.7.

See also

“A New C-API for Thread-Local Storage in CPython” ([**PEP 539**](https://peps.python.org/pep-0539/))

[Subject index](INDEX.md) · [Owning C API section and shared conditions](thread-local-storage-support.md) · [Following source contract](py-tss-t-to-py-tss-needs-init.md)
