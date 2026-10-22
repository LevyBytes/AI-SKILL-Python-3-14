# Not overriding `tp_free`

#### Not overriding `tp_free`

A heap type's [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot has to be assigned [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del). That is the default; leave it as is.

[Subject index](INDEX.md) · [Previous source context](defining-tp-dealloc.md) · [Following source context](avoiding-pyobject-new.md)
