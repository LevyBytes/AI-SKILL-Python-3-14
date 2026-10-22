# type objects C API: `Py_tp_token`, `Py_TP_USE_SPEC`

Py_tp_token

* Joined the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.14.*

A `slot` holding a class's static memory layout ID.

When a class has a statically allocated `PyType_Spec`, you can point the token at that spec via the special value `Py_TP_USE_SPEC`:

```c
static PyType_Slot foo_slots[] = {
   {Py_tp_token, Py_TP_USE_SPEC},

```

Alternatively you may point it at any pointer you like, provided you guarantee that:

- The class is outlived by the pointer, keeping it from being recycled elsewhere for as long as the class is around.

- It “belongs” to whichever extension module houses the class, ensuring no collision with other extensions.

Reach for `PyType_GetBaseByToken()` when you need to find out whether a particular token belongs to a class’s superclass — in other words, to confirm the memory layout lines up.

Retrieving the token of a class on its own (superclasses left aside) is done with `PyType_GetSlot()` paired with `Py_tp_token`.

Added in version 3.14.

 Py_TP_USE_SPEC

* Has been in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) starting from version 3.14.*

Paired with `Py_tp_token` as a value, this makes the token point at the class’s `PyType_Spec`. It expands to `NULL`.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytype-frommetaclass-to-pytype-fromspec.md) · [Owning structure and shared ABI conditions](pytype-slot-to-py-tp-doc.md)
