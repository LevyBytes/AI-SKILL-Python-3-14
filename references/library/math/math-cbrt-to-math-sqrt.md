# math - Power, exponential and logarithmic functions

### Power, exponential and logarithmic functions

 math.cbrt(*x*)

Give back the cube root of *x*.

Added in version 3.11.

 math.exp(*x*)

Give back *e* to the power *x*; here *e* = 2.718281… serves as the base for natural logarithms. Accuracy here usually beats `math.e ** x` or `pow(math.e, x)`.

 math.exp2(*x*)

Give back *2* raised to the power *x*.

Added in version 3.11.

 math.expm1(*x*)

Give back *e* raised to the power *x*, then minus 1. Here *e* is the base of natural logarithms. When *x* is a small float, the subtraction within `exp(x) - 1` can incur a [significant loss of precision](https://en.wikipedia.org/wiki/Loss_of_significance); the `expm1()` function lets you compute that quantity at full precision:

```python
>>> from math import exp, expm1
>>> exp(1e-5) - 1  # gives result accurate to 11 places
1.0000050000069649e-05
>>> expm1(1e-5)    # result accurate to full precision
1.0000050000166668e-05

```

Added in version 3.2.

 math.log(*x*[, *base*])

Given a single argument, give back the natural logarithm of *x* (to base *e*).

Given two arguments, give back the logarithm of *x* to the supplied *base*, worked out as `log(x)/log(base)`.

 math.log1p(*x*)

Give back the natural logarithm of *1+x* (base *e*). The computation stays accurate for *x* close to zero.

 math.log2(*x*)

Give back the base-2 logarithm of *x*. This tends to be more accurate than `log(x, 2)`.

Added in version 3.3.

See also

[`int.bit_length()`](https://docs.python.org/3.14/library/stdtypes.html#int.bit_length) gives how many bits a binary representation of an integer needs, leaving out the sign and any leading zeros.

 math.log10(*x*)

Give back the base-10 logarithm of *x*. This tends to be more accurate than `log(x, 10)`.

 math.pow(*x*, *y*)

Give back *x* raised to the power *y*. The exceptional cases track the IEEE 754 standard as closely as feasible. In particular, `pow(1.0, x)` and `pow(x, 0.0)` always give back `1.0`, even where *x* is a zero or a NaN. Should both *x* and *y* be finite while *x* is negative and *y* fails to be an integer, `pow(x, y)` has no defined value and raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

In contrast to the built-in `**` operator, `math.pow()` coerces both of its arguments to type [`float`](https://docs.python.org/3.14/library/functions.html#float). For exact integer powers, use `**` or the built-in `pow()` function.

Changed in version 3.11: To align with IEEE 754, the special cases `pow(0.0, -inf)` and `pow(-0.0, -inf)` now yield `inf` rather than raising [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 math.sqrt(*x*)

Give back the square root of *x*.

[Subject index](INDEX.md) · [Previous](math-ulp.md) · [Continue](math-dist-to-math-sumprod.md) · [Owning module, declaration or section: math](math-mathematical-functions.md)
