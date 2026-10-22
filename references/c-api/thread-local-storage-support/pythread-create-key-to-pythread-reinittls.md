# Legacy APIs

### Legacy APIs

Deprecated since version 3.7: The thread-specific storage (TSS) API now takes the place of this one.

Note

Platforms whose native TLS key is defined such that it cannot be cast to `int` safely are not handled by this version of the API. There, `PyThread_create_key()` fails and returns at once, and every other TLS function turns into a no-op.

Owing to the compatibility issue described above, fresh code should avoid this version of the API.

 int PyThread_create_key()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 void PyThread_delete_key(int key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 int PyThread_set_key_value(int key, void *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 void *PyThread_get_key_value(int key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 void PyThread_delete_key_value(int key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 void PyThread_ReInitTLS()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[Subject index](INDEX.md) · [Owning C API section and shared conditions](thread-local-storage-support.md) · [Previous source contract](pythread-tss-is-created-to-pythread-tss-get.md) · [Following source contract](../tuple-objects/pytupleobject-to-pytuple-setitem.md)
