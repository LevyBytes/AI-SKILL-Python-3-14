# math - Floating point arithmetic

### Floating point arithmetic

 math.ceil(*x*)

Give back the ceiling of *x* — that is, the least integer that is at least as large as *x*. When *x* is not a float, the work is delegated to [`x.__ceil__`](https://docs.python.org/3.14/reference/datamodel.html#object.__ceil__), which ought to return an [`Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral) value.

 math.fabs(*x*)

Give back the absolute value of *x*.

 math.floor(*x*)

Give back the floor of *x* — that is, the greatest integer no larger than *x*. When *x* is not a float, the work is delegated to [`x.__floor__`](https://docs.python.org/3.14/reference/datamodel.html#object.__floor__), which ought to return an [`Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral) value.

 math.fma(*x*, *y*, *z*)

Fused multiply-add operation. Give back `(x * y) + z`, evaluated as if at infinite precision and range and then subjected to one round into the `float` format. Accuracy from this operation frequently beats that of writing the expression `(x * y) + z` directly.

The behavior here matches the fusedMultiplyAdd operation spelled out by the IEEE 754 standard. That standard leaves a single case up to the implementation: the outcome of `fma(0, inf, nan)` and `fma(inf, 0, nan)`. For those, `math.fma` yields a NaN and raises nothing.

Added in version 3.13.

 math.fmod(*x*, *y*)

Give back the floating-point remainder of `x / y`, matching what the platform's C library routine `fmod(x, y)` produces. Keep in mind that Python's `x % y` expression can give a different answer. Per the C standard's intent, `fmod(x, y)` should be exactly (mathematically, at infinite precision) `x - n*y` for some integer *n* chosen so the result shares the sign of *x* and has magnitude under `abs(y)`. Python's `x % y`, by contrast, produces a result carrying the sign of *y*, and for float arguments it may not be exactly computable. To illustrate, `fmod(-1e-100, 1e100)` equals `-1e-100`, yet Python's `-1e-100 % 1e100` works out to `1e100-1e-100`, which has no exact float representation and rounds to the unexpected `1e100`. Because of this, prefer the `fmod()` function for float work, while Python's `x % y` suits integer work.

 math.modf(*x*)

Give back both the fractional and the integer pieces of *x*. Each piece is a float and carries the sign of *x*.

Be aware that `modf()` uses a calling and return convention unlike its C counterparts: it accepts a lone argument and hands back a pair, instead of routing a second return through an 'output parameter' (Python has no such mechanism).

 math.remainder(*x*, *y*)

Give back the IEEE 754-style remainder of *x* with respect to *y*. With *x* finite and *y* finite and nonzero, this equals the difference `x - n*y`, where `n` is whichever integer sits closest to the exact quotient `x / y`. When `x / y` lands exactly midway between two consecutive integers, the nearest *even* integer is used for `n`. So the remainder `r = remainder(x, y)` always meets `abs(r) <= 0.5 * abs(y)`.

The special cases obey IEEE 754: notably, `remainder(x, math.inf)` is *x* for every finite *x*, while `remainder(x, 0)` and `remainder(math.inf, x)` raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) for every non-NaN *x*. Whenever the remainder operation produces zero, that zero takes the sign of *x*.

On platforms with IEEE 754 binary floating point, this operation's result is always exactly representable, introducing no rounding error.

Added in version 3.7.

 math.trunc(*x*)

Give back *x* stripped of its fractional part, keeping only the integer part. The rounding goes toward 0: `trunc()` matches `floor()` for positive *x* and matches `ceil()` for negative *x*. When *x* is not a float, the work is delegated to [`x.__trunc__`](https://docs.python.org/3.14/reference/datamodel.html#object.__trunc__), which ought to return an [`Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral) value.

Regarding the `ceil()`, `floor()`, and `modf()` functions, observe that *every* floating-point number whose magnitude is large enough is already an exact integer. Python floats normally hold at most 53 bits of precision (matching the platform's C double type), and in that situation any float *x* with `abs(x) >= 2**52` is guaranteed to have no fractional bits.

[Subject index](INDEX.md) · [Previous](math-comb-to-math-perm.md) · [Continue](math-copysign-to-math-nextafter.md) · [Owning module, declaration or section: math](math-mathematical-functions.md)
