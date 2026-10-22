# Complex Numbers as Python Objects

### Complex Numbers as Python Objects

 type PyComplexObject

A subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) that stands for a Python complex number object.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyComplex_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An instance of [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) that stands for the Python complex number type. Over in the Python layer it is the very same object as [`complex`](https://docs.python.org/3.14/library/functions.html#complex).

 int PyComplex_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Hand back true when the argument is a `PyComplexObject` or a subtype of `PyComplexObject`. This function never fails.

 int PyComplex_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Hand back true when the argument is a `PyComplexObject` yet not a subtype of `PyComplexObject`. This function never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyComplex_FromCComplex(Py_complex v)

*Return value: New reference.*

Build a fresh Python complex number object out of a C `Py_complex` value. On error, hand back `NULL` with an exception set.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyComplex_FromDoubles(double real, double imag)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a fresh `PyComplexObject` object built from *real* and *imag*. On error, hand back `NULL` with an exception set.

 double PyComplex_RealAsDouble([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the real part of *op* as a C double.

Where *op* is not a Python complex number object yet carries a [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) method, that method gets invoked first to turn *op* into a Python complex number object. Where `__complex__()` is undefined, it instead drops down to calling [`PyFloat_AsDouble()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_AsDouble) and hands back that result.

On failure, this method hands back `-1.0` with an exception set, so you ought to call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to check for errors.

Changed in version 3.13: Use [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) if available.

 double PyComplex_ImagAsDouble([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the imaginary part of *op* as a C double.

Where *op* is not a Python complex number object yet carries a [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) method, that method gets invoked first to turn *op* into a Python complex number object. Where `__complex__()` is undefined, it instead drops down to calling [`PyFloat_AsDouble()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_AsDouble) and hands back `0.0` on success.

On failure, this method hands back `-1.0` with an exception set, so you ought to call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to check for errors.

Changed in version 3.13: Use [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) if available.

 Py_complex PyComplex_AsCComplex([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Hand back the `Py_complex` value of the complex number *op*.

Where *op* is not a Python complex number object yet carries a [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) method, that method gets invoked first to turn *op* into a Python complex number object. Where `__complex__()` is undefined, it drops down to [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__); and where `__float__()` is undefined, it drops down further to [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__).

On failure, this method hands back a `Py_complex` whose `real` is set to `-1.0`, with an exception set, so you ought to call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to check for errors.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](complex-number-objects.md) · [Previous source contract](py-complex-to-py-c-pow.md)
