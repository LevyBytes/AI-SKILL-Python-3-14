# PyMemberDef.doc and shared member access, offset and slot conditions

const char *doc

The docstring, or NULL. Keep the string static; nothing copies it. It is typically built with [`PyDoc_STR`](https://docs.python.org/3.14/c-api/intro.html#c.PyDoc_STR).

By default ? that is, with `flags` set to `0` ? members permit reading as well as writing. To restrict to read-only, apply the `Py_READONLY` flag. A few types, `Py_T_STRING` among them, carry an implied `Py_READONLY`. Deletion works only on `Py_T_OBJECT_EX` members (plus the legacy `T_OBJECT`).

On heap-allocated types (those made via [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec) and the like), a `PyMemberDef` may hold a definition for the special member `"__vectorcalloffset__"`, which lines up with [`tp_vectorcall_offset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset) in type objects. You have to define this member using `Py_T_PYSSIZET` together with either `Py_READONLY` or `Py_READONLY | Py_RELATIVE_OFFSET`. As an example:

```c
static PyMemberDef spam_type_members[] = {
    {"__vectorcalloffset__", Py_T_PYSSIZET,
     offsetof(Spam_object, vectorcall), Py_READONLY},
    {NULL}  /* Sentinel */
};

```

(Pulling in `offsetof()` may require you to `#include <stddef.h>`.)
You can set up the older [`tp_dictoffset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset) and [`tp_weaklistoffset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset) offsets in much the same fashion, by way of `"__dictoffset__"` and `"__weaklistoffset__"` members; even so, the firm recommendation for extensions is to reach for [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) and [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF) in their place.

Changed in version 3.12: `PyMemberDef` can now be relied on at all times; earlier releases made you pull in `"structmember.h"` first.

Changed in version 3.14: `Py_RELATIVE_OFFSET` may now be applied to `"__vectorcalloffset__"`, `"__dictoffset__"` and `"__weaklistoffset__"`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymemberdef-to-flags.md) · [Previous source contract](pymember-getone.md)
