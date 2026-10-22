# thread local storage support C API: `Py_tss_t`, `Py_tss_NEEDS_INIT`

type Py_tss_t

This structure captures a thread key's state; its exact definition can vary with the underlying TLS implementation, and it carries an internal field that tracks whether the key has been initialized. The structure exposes no public members.

Provided [Py_LIMITED_API](https://docs.python.org/3.14/c-api/stable.html#stable) is not defined, you may statically allocate this type via `Py_tss_NEEDS_INIT`.

 Py_tss_NEEDS_INIT

The initializer for `Py_tss_t` variables is produced by expanding this macro. Be aware that the macro stays undefined whenever [Py_LIMITED_API](https://docs.python.org/3.14/c-api/stable.html#stable) is in effect.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](thread-local-storage-support.md) · [Owning C API section and shared conditions](thread-specific-storage-api.md) · [Following source contract](pythread-tss-alloc-to-pythread-tss-free.md)
