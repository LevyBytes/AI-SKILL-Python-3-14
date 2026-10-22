# Methods

### Methods

For these functions, the *key* parameter must never be `NULL`. Furthermore, calling `PyThread_tss_set()` or `PyThread_tss_get()` produces undefined behavior when the supplied `Py_tss_t` has not yet been initialized through `PyThread_tss_create()`.

 int PyThread_tss_is_created(Py_tss_t *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Hand back a non-zero value when the supplied `Py_tss_t` has already been initialized by `PyThread_tss_create()`.

 int PyThread_tss_create(Py_tss_t *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Hand back a zero value once a TSS key has been initialized successfully. Behavior is undefined when the value the *key* argument points at was not initialized by `Py_tss_NEEDS_INIT`. You may call this repeatedly against the same key – invoking it on a key that is already initialized does nothing and returns success right away.

 void PyThread_tss_delete(Py_tss_t *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Tear down a TSS key so the values bound to it across every thread are forgotten, and switch the key's initialization state back to uninitialized. A torn-down key can be initialized once more via `PyThread_tss_create()`. You may call this repeatedly against the same key – invoking it on a key that is already destroyed does nothing.

 int PyThread_tss_set(Py_tss_t *key, void *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Hand back a zero value to report that a void* value was bound to a TSS key for the current thread. Every thread keeps its own separate mapping from the key to a void* value.

 void *PyThread_tss_get(Py_tss_t *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Hand back the void* value bound to a TSS key for the current thread. The result is `NULL` when the current thread has no value bound to the key.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](thread-local-storage-support.md) · [Previous source contract](pythread-tss-alloc-to-pythread-tss-free.md) · [Following source contract](pythread-create-key-to-pythread-reinittls.md)
