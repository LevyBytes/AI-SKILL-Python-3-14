# type slots C API: Allocation, destructor, traversal and hash callback typedefs

### Slot Type typedefs

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*allocfunc)([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *cls, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) nitems)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

What this function aims to do is keep memory allocation apart from memory initialization. It ought to return a pointer to a memory block of sufficient length for the instance, properly aligned, and zero-filled, except that [`ob_refcnt`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_refcnt) is set to `1` and [`ob_type`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_type) is set to the type argument. When the type's `tp_itemsize` is nonzero, the object's [`ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size) field ought to be initialized to *nitems*, and the allocated memory block's length ought to be `tp_basicsize + nitems*tp_itemsize`, rounded up to a multiple of `sizeof(void*)`; otherwise *nitems* goes unused and the block's length ought to be `tp_basicsize`.

This function ought to perform no further instance initialization, not so much as allocating extra memory; `tp_new` is where that belongs.

 typedef void (*destructor)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 typedef void (*freefunc)(void*)

See `tp_free`.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*newfunc)([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_new`.

 typedef int (*initproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_init`.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*reprfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_repr`.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*getattrfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *self, char *attr)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the value of the object's named attribute.

 typedef int (*setattrfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *self, char *attr, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign the value of the object's named attribute. Passing `NULL` as the value argument deletes the attribute.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*getattrofunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *self, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the value of the object's named attribute.

See `tp_getattro`.

 typedef int (*setattrofunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *self, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *attr, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign the value of the object's named attribute. Passing `NULL` as the value argument deletes the attribute.

See `tp_setattro`.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*descrgetfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_descr_get`.

 typedef int (*descrsetfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_descr_set`.

 typedef [Py_hash_t](https://docs.python.org/3.14/c-api/hash.html#c.Py_hash_t) (*hashfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

See `tp_hash`.

[Subject index](INDEX.md) · [Previous source contract](pyasyncmethods-to-pyasyncmethods-am-send.md) · [Following source contract](pyobject-to-pysendresult.md)
