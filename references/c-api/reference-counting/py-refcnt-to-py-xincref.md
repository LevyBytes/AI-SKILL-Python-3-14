# reference counting C API: `Py_REFCNT()`, `Py_SET_REFCNT()`, `Py_INCREF()`, `Py_XINCREF()`

# Refcounting, Reflection

## Overview

Covers: Reference Counting; Reflection.

## Reference Counting

### Reference Counting

The routines and macros gathered in this section handle the bookkeeping of reference counts for Python objects.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) Py_REFCNT([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Fetch the reference count belonging to the Python object *o*.

Keep in mind that the value handed back might not truly correspond to the count of references currently held against the object. As an illustration, certain objects are [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) and carry an extremely high refcount that bears no relation to how many references really exist. For that reason, treat any returned figure besides 0 or 1 as unreliable.

Call the `Py_SET_REFCNT()` function to assign an object's reference count.

Note

Under [free-threaded builds](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) of Python, a result of 1 does not by itself prove it is safe to regard *o* as untouched by any other thread. Reach for [`PyUnstable_Object_IsUniquelyReferenced()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_Object_IsUniquelyReferenced) in that scenario instead.

Also consult the function [`PyUnstable_Object_IsUniqueReferencedTemporary()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_Object_IsUniqueReferencedTemporary).

Changed in version 3.10: `Py_REFCNT()` is changed to the inline static function.

Changed in version 3.11: The parameter type is no longer const [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 void Py_SET_REFCNT([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) refcnt)

Assign the value *refcnt* to the reference counter of object *o*.

Under a [Python build with Free Threading](https://docs.python.org/3.14/using/configure.html#free-threading-build), should *refcnt* exceed `UINT32_MAX`, the object becomes [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

The function leaves [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) objects untouched.

Added in version 3.9.

Changed in version 3.12: Immortal objects are not modified.

 void Py_INCREF([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Signal that you are acquiring a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to object *o*, marking it as live and not eligible for destruction.

The function leaves [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) objects untouched.

This routine is most often applied to turn a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) into a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) in place. To mint a brand-new strong reference, you can instead reach for the `Py_NewRef()` function.

After you have finished with the object, free it by calling `Py_DECREF()`.

The object cannot be `NULL`; when you are uncertain whether it is `NULL`, fall back on `Py_XINCREF()`.

Do not count on this function to alter *o* in any fashion. For at least [**some objects**](https://peps.python.org/pep-0683/), it does nothing at all.

Changed in version 3.12: Immortal objects are not modified.

 void Py_XINCREF([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Comparable to `Py_INCREF()`, except that here the object *o* is allowed to be `NULL`, in which event nothing happens.

Also consult `Py_XNewRef()`.

[Subject index](INDEX.md) · [Following source contract](py-newref-to-py-decref.md)
