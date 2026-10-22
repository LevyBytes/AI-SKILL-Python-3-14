# Py_hash_t PyObject_HashNotImplemented(PyObject *o)

[Py_hash_t](https://docs.python.org/3.14/c-api/hash.html#c.Py_hash_t) PyObject_HashNotImplemented([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) signaling that `type(o)` is not [hashable](https://docs.python.org/3.14/glossary.html#term-hashable), then return `-1`. When placed in a `tp_hash` slot, this function is handled specially: it lets a type announce to the interpreter, in explicit terms, that instances cannot be hashed.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Following source contract](pyobject-hash.md) · [Following source contract](pyobject-istrue-to-pyobject-selfiter.md)
