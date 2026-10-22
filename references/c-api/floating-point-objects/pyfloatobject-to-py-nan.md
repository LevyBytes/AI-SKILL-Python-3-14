# floating point objects C API: Floating-point construction, conversion and special values

# Float, Frame

## Overview

Covers: Floating-Point Objects; Frame objects.

## Floating-Point Objects

### Floating-Point Objects

 type PyFloatObject

Standing in for a Python floating-point object, this is a subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyFloat_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Standing in for the Python floating-point type, this is a [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance. Over in the Python layer it is the very same object as [`float`](https://docs.python.org/3.14/library/functions.html#float).

 int PyFloat_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Hand back true whenever the supplied argument is a `PyFloatObject`, or else a subtype of `PyFloatObject`. Success is guaranteed for this routine.

 int PyFloat_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Hand back true whenever the supplied argument is a `PyFloatObject` yet not a subtype of `PyFloatObject`. Success is guaranteed for this routine.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFloat_FromString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *str)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a `PyFloatObject` object out of the string value held in *str*, or `NULL` should it fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFloat_FromDouble(double v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a `PyFloatObject` object out of *v*, or `NULL` should it fail.

 double PyFloat_AsDouble([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pyfloat)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a C double rendering of whatever *pyfloat* holds. Where *pyfloat* is not a Python floating-point object but does carry a [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) method, that method is invoked first to turn *pyfloat* into a float. Where `__float__()` is undefined, it drops back to [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__). On failure this method hands back `-1.0`, so you ought to call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to test for errors.

Changed in version 3.8: Reach for [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) where it is on hand.

 double PyFloat_AS_DOUBLE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pyfloat)

Hand back a C double rendering of whatever *pyfloat* holds, this time skipping any error checking.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFloat_GetInfo(void)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a structseq instance carrying details on a float's precision together with its smallest and largest values. It amounts to a thin wrapper over the `float.h` header file.

 double PyFloat_GetMax()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back, as a C double, the largest representable finite float *DBL_MAX*.

 double PyFloat_GetMin()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back, as a C double, the smallest normalized positive float *DBL_MIN*.

 Py_INFINITY

Standing for positive infinity, this macro expands into a constant expression whose type is double.

Across most platforms it amounts to the `INFINITY` macro out of the C11 standard `<math.h>` header.

 Py_NAN

Standing for a quiet not-a-number (qNaN) value, this macro expands into a constant expression whose type is double.

Across most platforms it amounts to the `NAN` macro out of the C11 standard `<math.h>` header.

[Subject index](INDEX.md) · [Following source contract](py-huge-val-to-py-is-nan.md)
