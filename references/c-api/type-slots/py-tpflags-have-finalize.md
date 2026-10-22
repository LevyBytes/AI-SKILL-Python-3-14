# Py_TPFLAGS_HAVE_FINALIZE

Py_TPFLAGS_HAVE_FINALIZE

This bit gets enabled whenever the type structure includes the `tp_finalize` slot.

Added in version 3.4.

Deprecated since version 3.8: The flag is no longer required, because the interpreter now treats the `tp_finalize` slot as if it is always part of the type structure.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Following source contract](py-tpflags-long-subclass-to-py-tpflags-type-subclass.md) · [Following source contract](py-tpflags-have-vectorcall-to-py-tpflags-mapping.md)
