# math: `math.ulp()`

math.ulp(*x*)

Give back the value of the least significant bit belonging to the float *x*:

- When *x* is a NaN (not a number), give back *x*.

- When *x* is negative, give back `ulp(-x)`.

- When *x* is a positive infinity, give back *x*.

- When *x* equals zero, give back the smallest positive *denormalized* representable float (below the minimum positive *normalized* float, [`sys.float_info.min`](https://docs.python.org/3.14/library/sys.html#sys.float_info)).

- When *x* equals the largest positive representable float, give back the bit weight at the bottom of *x*, chosen so the nearest float below *x* equals `x - ulp(x)`.

- In every other case (*x* being a positive finite number), give back the bit weight at the bottom of *x*, chosen so the nearest float above *x* equals `x + ulp(x)`.

ULP stands for “Unit in the Last Place”.

See also `math.nextafter()` and [`sys.float_info.epsilon`](https://docs.python.org/3.14/library/sys.html#sys.float_info).

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](math-copysign-to-math-nextafter.md) · [Continue](math-cbrt-to-math-sqrt.md) · [Owning module, declaration or section: math](math-mathematical-functions.md) · [Owning module, declaration or section: Floating point manipulation functions](math-copysign-to-math-nextafter.md)
