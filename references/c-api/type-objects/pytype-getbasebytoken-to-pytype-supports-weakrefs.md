# type objects C API: `PyType_GetBaseByToken()`, `PyUnstable_Type_AssignVersionTag()`, `PyType_SUPPORTS_WEAKREFS()`

int PyType_GetBaseByToken(PyTypeObject *type, void *token, PyTypeObject **result)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Locate the first superclass in *type*'s [method resolution order](https://docs.python.org/3.14/glossary.html#term-method-resolution-order) whose `Py_tp_token` token matches the one you pass in.

- When it is found, point **result* at a new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to it and return `1`.

- When it is not found, point **result* at `NULL` and return `0`.

- On error, point **result* at `NULL` and return `-1` with an exception set.

You may pass `NULL` for the *result* argument, in which case **result* is left untouched. Do this whenever the return value alone is enough for you.

The *token* argument may not be `NULL`.

Added in version 3.14.

 int PyUnstable_Type_AssignVersionTag(PyTypeObject *type)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Try to give the supplied type a version tag.

Returns 1 when the type already carried a valid version tag or a new one got assigned, and 0 when no new tag could be assigned.

Added in version 3.12.

 int PyType_SUPPORTS_WEAKREFS(PyTypeObject *type)

Returns true when instances of *type* can have weak references created for them, and false otherwise. The call never fails. *type* may not be `NULL`.

See also

- [Weak Reference Objects](https://docs.python.org/3.14/c-api/weakref.html#weakrefobjects)

- [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref)

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-to-pytype-watch.md) · [Previous source contract](pytype-getfullyqualifiedname-to-pytype-getmodulebydef.md) · [Following source contract](pytype-frommetaclass-to-pytype-fromspec.md)
