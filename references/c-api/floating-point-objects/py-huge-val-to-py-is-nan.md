# floating point objects C API: `Py_HUGE_VAL`, `Py_MATH_E`, `Py_MATH_El`, `Py_MATH_PI`, `Py_MATH_PIl`, `Py_MATH_TAU`, `Py_RETURN_NAN`, `Py_RETURN_INF()`, `Py_IS_FINITE()`, `Py_IS_INFINITY()`, `Py_IS_NAN()`

Py_HUGE_VAL

Equivalent to `INFINITY`.

Deprecated since version 3.14: This macro now counts as [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated).

 Py_MATH_E

How the [`math.e`](https://docs.python.org/3.14/library/math.html#math.e) constant is defined, to double-type accuracy.

 Py_MATH_El

A high-precision (long double) definition of the [`e`](https://docs.python.org/3.14/library/math.html#math.e) constant.

 Py_MATH_PI

How the [`math.pi`](https://docs.python.org/3.14/library/math.html#math.pi) constant is defined, to double-type accuracy.

 Py_MATH_PIl

A high-precision (long double) definition of the [`pi`](https://docs.python.org/3.14/library/math.html#math.pi) constant.

 Py_MATH_TAU

How the [`math.tau`](https://docs.python.org/3.14/library/math.html#math.tau) constant is defined, to double-type accuracy.

Added in version 3.6.

 Py_RETURN_NAN

Hand [`math.nan`](https://docs.python.org/3.14/library/math.html#math.nan) back out of a function.

Across most platforms it amounts to `return PyFloat_FromDouble(NAN)`.

 Py_RETURN_INF(sign)

Hand either [`math.inf`](https://docs.python.org/3.14/library/math.html#math.inf) or `-math.inf` back out of a function, the choice hinging on the sign of *sign*.

Across most platforms it amounts to what follows:

```c
return PyFloat_FromDouble(copysign(INFINITY, sign));

```

 Py_IS_FINITE(X)

Hand back `1` whenever the supplied floating-point number *X* is finite — meaning normal, subnormal or zero, but neither infinite nor NaN. Otherwise hand back `0`.

Deprecated since version 3.14: This macro now counts as [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Turn to `isfinite` in its place.

 Py_IS_INFINITY(X)

Hand back `1` whenever the supplied floating-point number *X* is infinity, whether positive or negative. Otherwise hand back `0`.

Deprecated since version 3.14: This macro now counts as [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Turn to `isinf` in its place.

 Py_IS_NAN(X)

Hand back `1` whenever the supplied floating-point number *X* is a not-a-number (NaN) value. Otherwise hand back `0`.

Deprecated since version 3.14: This macro now counts as [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Turn to `isnan` in its place.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyfloatobject-to-py-nan.md) · [Following source contract](pack-and-unpack-functions.md)
