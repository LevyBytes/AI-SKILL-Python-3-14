# int PyUnstable_Object_IsUniquelyReferenced(PyObject *op)

int PyUnstable_Object_IsUniquelyReferenced([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Work out whether *op* holds just one reference.

Within GIL-enabled builds, this call is the same as [Py_REFCNT](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT)(op) == 1.

Within a [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), it tests whether *op*'s [reference count](https://docs.python.org/3.14/glossary.html#term-reference-count) equals one and, on top of that, confirms that *op* is used only by the current thread. Because [Py_REFCNT](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT)(op) == 1 is **not** thread-safe on free-threaded builds, favor this function instead.

Even though this function never enters the Python interpreter, the caller still has to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). This function cannot fail.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](pyunstable-tryincref-to-pyunstable-enabletryincref.md)
