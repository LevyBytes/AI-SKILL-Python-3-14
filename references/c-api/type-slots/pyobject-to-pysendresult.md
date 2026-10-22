# type slots C API: Comparison, iteration, descriptor and send callback typedefs

typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*richcmpfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, int)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_richcompare`.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*getiterfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_iter`.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*iternextfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_iternext`.

 typedef [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) (*lenfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef int (*getbufferproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [Py_buffer](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer)*, int)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

 typedef void (*releasebufferproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [Py_buffer](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*unaryfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*binaryfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef [PySendResult](https://docs.python.org/3.14/c-api/iter.html#c.PySendResult) (*sendfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)**)

See `am_send`.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*ternaryfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*ssizeargfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t))

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef int (*ssizeobjargproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t), [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef int (*objobjproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef int (*objobjargproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyobject-to-py-hash-t.md) · [Following source contract](examples-pyobject-head.md)
