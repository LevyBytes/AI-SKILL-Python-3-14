# Dynamic allocation

### Dynamic allocation

Dynamically allocating the `Py_tss_t` becomes necessary in extension modules compiled with [Py_LIMITED_API](https://docs.python.org/3.14/c-api/stable.html#stable), because static allocation of the type is impossible there given that its implementation stays opaque at build time.

 Py_tss_t *PyThread_tss_alloc()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Hand back a value carrying the same state as one initialized with `Py_tss_NEEDS_INIT`, or `NULL` should the dynamic allocation fail.

 void PyThread_tss_free(Py_tss_t *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Release the supplied *key* that `PyThread_tss_alloc()` allocated, having first invoked `PyThread_tss_delete()` so that any attached thread locals are unassigned. When the *key* argument is `NULL`, this does nothing.

Note

Once freed, a key turns into a dangling pointer. Set the key back to `NULL`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](thread-local-storage-support.md) · [Previous source contract](py-tss-t-to-py-tss-needs-init.md) · [Following source contract](pythread-tss-is-created-to-pythread-tss-get.md)
