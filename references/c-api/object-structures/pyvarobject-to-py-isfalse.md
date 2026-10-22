# object structures C API: `PyVarObject`, `PyObject_HEAD`, `PyObject_VAR_HEAD`, `PyBaseObject_Type`, `Py_Is()`, `Py_IsNone()`, `Py_IsTrue()`, `Py_IsFalse()`

type PyVarObject

* Part of the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable). (Only some members are part of the stable ABI.)*

A `PyObject` variant that tacks on the `ob_size` field. It suits objects that carry some idea of *length*.

Just like `PyObject`, you must not poke at the members directly; lean on macros such as `Py_SIZE`, [`Py_REFCNT`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) and `Py_TYPE`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) ob_size

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is a size field; treat whatever it holds as an internal implementation detail of the object.

Skip accessing the field straight on; reach for `Py_SIZE` instead.

When an object is built ? for instance through [`PyObject_NewVar()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar) ? this field usually gets set to the size that was asked for (the count of items). Once the object exists, you may stash whatever values you like in `ob_size` by way of `Py_SET_SIZE`.

When you want an object's publicly visible length ? the figure the Python [`len()`](https://docs.python.org/3.14/library/functions.html#len) function reports ? call [`PyObject_Length()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Length) instead.

 PyObject_HEAD

Reach for this macro while declaring fresh types whose objects have no length that varies. The PyObject_HEAD macro expands to:

```c
PyObject ob_base;

```

Refer to the `PyObject` documentation above.

 PyObject_VAR_HEAD

Reach for this macro while declaring fresh types whose objects carry a length differing from one instance to the next. The PyObject_VAR_HEAD macro expands to:

```c
PyVarObject ob_base;

```

Refer to the `PyVarObject` documentation above.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyBaseObject_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Every other object descends from this base class ? it is the equivalent of [`object`](https://docs.python.org/3.14/library/functions.html#object) in Python.

 int Py_Is(PyObject *x, PyObject *y)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Check whether the *x* object and the *y* object are one and the same ? equivalent to `x is y` in Python.

Added in version 3.10.

 int Py_IsNone(PyObject *x)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Check whether an object is the `None` singleton ? equivalent to `x is None` in Python.

Added in version 3.10.

 int Py_IsTrue(PyObject *x)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Check whether an object is the `True` singleton ? equivalent to `x is True` in Python.

Added in version 3.10.

 int Py_IsFalse(PyObject *x)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Check whether an object is the `False` singleton ? equivalent to `x is False` in Python.

Added in version 3.10.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](base-object-types-and-macros.md) · [Previous source contract](pyobject-to-ob-refcnt.md) · [Following source contract](py-type-to-pyvarobject-head-init.md)
