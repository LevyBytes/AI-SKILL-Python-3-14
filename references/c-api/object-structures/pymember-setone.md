# int PyMember_SetOne(char *obj_addr, struct PyMemberDef *m, PyObject *o)

int PyMember_SetOne(char *obj_addr, struct PyMemberDef *m, PyObject *o)

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign the value *o* to an attribute held by the object located at *obj_addr*. The attribute being written is the one spelled out by `PyMemberDef` *m*. A success yields `0`, while a failure yields some negative number.

Changed in version 3.12: `PyMember_SetOne` can now be used unconditionally; before that you had to bring in `"structmember.h"`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymemberdef-to-flags.md) · [Previous source contract](pymember-getone.md) · [Following source contract](py-readonly-to-py-relative-offset.md)
