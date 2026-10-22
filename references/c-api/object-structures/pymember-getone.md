# PyObject *PyMember_GetOne(const char *obj_addr, struct PyMemberDef *m)

PyObject *PyMember_GetOne(const char *obj_addr, struct PyMemberDef *m)

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Retrieve an attribute held by the object located at *obj_addr*. That attribute is the one spelled out by `PyMemberDef` *m*. Should something fail, the result is `NULL`.

Changed in version 3.12: `PyMember_GetOne` can now be used unconditionally; before that you had to bring in `"structmember.h"`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymemberdef-to-flags.md) · [Following source contract](doc.md) · [Following source contract](pymember-setone.md)
