# Py_hash_t PyObject_Hash(PyObject *o)

[Py_hash_t](https://docs.python.org/3.14/c-api/hash.html#c.Py_hash_t) PyObject_Hash([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Compute the hash value of an object *o* and return it. On failure, return `-1`. The behavior matches the Python expression `hash(o)`.
Changed in version 3.2: The return type has become Py_hash_t, a signed integer whose width matches [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](pyobject-str-to-pyobject-isinstance.md) · [Previous source contract](pyobject-hashnotimplemented.md)
