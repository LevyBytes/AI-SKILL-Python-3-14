# Member flags

### Member flags

The flags listed here are the ones you may apply to `PyMemberDef.flags`:

 Py_READONLY

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.12.*

Not writable.

 Py_AUDIT_READ

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.12.*

Fire an `object.__getattr__` [audit event](https://docs.python.org/3.14/library/audit_events.html#audit-events) ahead of the read.

 Py_RELATIVE_OFFSET

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.12.*

Signals that the `offset` recorded in this `PyMemberDef` entry is measured from the subclass-specific data instead of from `PyObject`.

This is valid solely inside the [`Py_tp_members`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_members) [`slot`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) while building a class with a negative [`basicsize`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec.basicsize), and there it is required. As the slot feeds [`tp_members`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_members) during class creation, Python drops the flag and rewrites `PyMemberDef.offset` so it counts from the `PyObject` struct.

Changed in version 3.10: The `RESTRICTED`, `READ_RESTRICTED` and `WRITE_RESTRICTED` macros that come with `#include "structmember.h"` are now deprecated. Both `READ_RESTRICTED` and `RESTRICTED` mean the same thing as `Py_AUDIT_READ`, whereas `WRITE_RESTRICTED` has no effect at all.

Changed in version 3.12: `READONLY` became `Py_READONLY`, and `PY_AUDIT_READ` picked up the `Py_` prefix as well. These newer spellings can now be used at any time, whereas they once needed `#include "structmember.h"`. That header has not gone away and still supplies the former names.

[Subject index](INDEX.md) · [Previous source contract](pymember-setone.md) · [Following source contract](member-types.md)
