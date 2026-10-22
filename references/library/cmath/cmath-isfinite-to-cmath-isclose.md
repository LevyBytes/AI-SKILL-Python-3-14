# cmath — Classification functions

### Classification functions

 cmath.isfinite(*z*)

Return `True` when both the real and the imaginary parts of *z* are finite; otherwise return `False`.

Added in version 3.2.

 cmath.isinf(*z*)

Return `True` when either the real or the imaginary part of *z* is an infinity; otherwise return `False`.

 cmath.isnan(*z*)

Return `True` when either the real or the imaginary part of *z* is a NaN; otherwise return `False`.

 cmath.isclose(*a*, *b*, ***, *rel_tol=1e-09*, *abs_tol=0.0*)

Return `True` when the values *a* and *b* lie close to each other, and `False` otherwise.

Closeness between two values is judged against supplied absolute and relative tolerances. Provided no errors arise, the outcome follows: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.

*rel_tol* is the relative tolerance — the largest permitted gap between *a* and *b*, scaled against whichever of *a* or *b* has the greater absolute value. As an example, a 5% tolerance comes from passing `rel_tol=0.05`. Its default of `1e-09` guarantees agreement of the two values to roughly 9 decimal digits. *rel_tol* has to be nonnegative and below `1.0`.

*abs_tol* is the absolute tolerance; its default is `0.0` and it must be nonnegative. In a comparison of `x` against `0.0`, `isclose(x, 0)` evaluates as `abs(x) <= rel_tol * abs(x)`, which comes out `False` for every `x` and rel_tol below `1.0`. For that reason, supply a suitable positive abs_tol argument in the call.

The IEEE 754 special values `NaN`, `inf`, and `-inf` are treated per IEEE rules. In particular, `NaN` counts as close to no other value at all, `NaN` included. `inf` and `-inf` count as close only to themselves.

Added in version 3.5.

See also

[**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality

[Subject index](INDEX.md) · [Previous](cmath-acosh-to-cmath-tanh.md) · [Continue](cmath-pi-to-cmath-nanj.md) · [Owning module, declaration or section: cmath](cmath-mathematical-functions-for-complex-numbers.md)
