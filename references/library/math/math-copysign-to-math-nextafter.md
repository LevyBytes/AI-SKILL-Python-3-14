# math: `math.copysign()`, `math.frexp()`, `math.isclose()`, `math.isfinite()`, `math.isinf()`, `math.isnan()`, `math.ldexp()`, `math.nextafter()`

### Floating point manipulation functions

 math.copysign(*x*, *y*)

Give back a float whose magnitude (absolute value) comes from *x* but whose sign comes from *y*. Where signed zeros are supported, `copysign(1.0, -0.0)` gives *-1.0*.

 math.frexp(*x*)

Give back the mantissa and exponent of *x* as the pair `(m, e)`. When *x* is a finite nonzero number, *m* is a float meeting `0.5 <= abs(m) < 1.0` and *e* is an integer making `x == m * 2**e` hold exactly. Otherwise, give back `(x, 0)`. This serves to “pick apart” a float's internal representation portably.

Be aware that `frexp()` uses a calling and return convention unlike its C counterparts: it accepts a lone argument and hands back a pair, instead of routing a second return through an 'output parameter' (Python has no such mechanism).

 math.isclose(*a*, *b*, ***, *rel_tol=1e-09*, *abs_tol=0.0*)

Give back `True` when the values *a* and *b* sit close to one another, and `False` otherwise.

Closeness gets decided from supplied absolute and relative tolerances. Absent any error, the outcome is: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.

*rel_tol* is the relative tolerance – the largest permitted gap between *a* and *b*, scaled against the bigger absolute value among *a* and *b*. As an example, a 5% tolerance is set by passing `rel_tol=0.05`. Its default is `1e-09`, which guarantees agreement of the two values to roughly 9 decimal digits. *rel_tol* has to be nonnegative and below `1.0`.

*abs_tol* is the absolute tolerance; its default is `0.0` and it has to be nonnegative. For a comparison of `x` against `0.0`, `isclose(x, 0)` reduces to `abs(x) <= rel_tol * abs(x)`, which is `False` for every nonzero `x` whenever *rel_tol* stays under `1.0`. So supply a fitting positive *abs_tol* argument to the call.

The IEEE 754 special values `NaN`, `inf`, and `-inf` follow IEEE rules here. Concretely, `NaN` counts as close to nothing else, not even another `NaN`. `inf` and `-inf` count as close only to themselves.

Added in version 3.5.

See also

[**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality

 math.isfinite(*x*)

Give back `True` whenever *x* is not an infinity and not a NaN; otherwise give back `False`. (Keep in mind that `0.0` *does* count as finite.)

Added in version 3.2.

 math.isinf(*x*)

Give back `True` when *x* is a positive or negative infinity, and `False` otherwise.

 math.isnan(*x*)

Give back `True` when *x* is a NaN (not a number), and `False` otherwise.

 math.ldexp(*x*, *i*)

Give back `x * (2**i)`. This essentially undoes the function `frexp()`.

 math.nextafter(*x*, *y*, *steps=1*)

Give back the floating-point value *steps* steps after *x* towards *y*.

Should *x* equal *y*, give back *y*, except when *steps* is zero.

Examples:

- `math.nextafter(x, math.inf)` goes up: towards positive infinity.

- `math.nextafter(x, -math.inf)` goes down: towards minus infinity.

- `math.nextafter(x, 0.0)` goes towards zero.

- `math.nextafter(x, math.copysign(math.inf, x))` goes away from zero.

See also `math.ulp()`.

Added in version 3.9.

Changed in version 3.12: Added the *steps* argument.

[Subject index](INDEX.md) · [Previous](math-ceil-to-math-trunc.md) · [Continue](math-ulp.md) · [Owning module, declaration or section: math](math-mathematical-functions.md)
