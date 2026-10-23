# math - Summation and product functions

### Summation and product functions

 math.dist(*p*, *q*)

Give back the Euclidean distance separating two points *p* and *q*, each supplied as a sequence (or iterable) of coordinates. Both points are required to share the same dimension.

Roughly equivalent to:

```python
sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

```

Added in version 3.8.

 math.fsum(*iterable*)

Give back an accurate floating-point sum over the values in the iterable. It dodges precision loss by keeping track of several intermediate partial sums.

How accurate the algorithm is depends on IEEE-754 arithmetic guarantees and on the common situation where rounding runs in half-even mode. On certain non-Windows builds, the underlying C library performs extended precision addition and might now and then double-round an intermediate sum, leaving it off by its least significant bit.

For more discussion plus two alternative approaches, consult the [ASPN cookbook recipes for accurate floating-point summation](https://code.activestate.com/recipes/393090-binary-floating-point-summation-accurate-to-full-p/).

 math.hypot(**coordinates*)

Give back the Euclidean norm, `sqrt(sum(x**2 for x in coordinates))`. That is the length of the vector running from the origin out to the point named by the coordinates.

For a two dimensional point `(x, y)`, this matches finding the hypotenuse of a right triangle via the Pythagorean theorem, `sqrt(x*x + y*y)`.

Changed in version 3.8: Gained support for n-dimensional points. Previously only the two dimensional case worked.

Changed in version 3.10: Sharpened the algorithm so its maximum error stays below 1 ulp (unit in the last place). In the common case the result is nearly always correctly rounded to within 1/2 ulp.

 math.prod(*iterable*, ***, *start=1*)

Work out the product of every element within the input *iterable*. By default the *start* value for that product is `1`.

When the iterable holds nothing, give back the start value. This function targets numeric values specifically and may turn away non-numeric types.

Added in version 3.8.

 math.sumprod(*p*, *q*)

Give back the sum of the products of values drawn from two iterables *p* and *q*.

Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) if the inputs do not have the same length.

Roughly equivalent to:

```python
sum(map(operator.mul, p, q, strict=True))

```

When inputs are floats or a mix of ints and floats, extended precision is used for the intermediate products and sums.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](math-cbrt-to-math-sqrt.md) · [Continue](math-degrees-to-math-radians.md) · [Owning module, declaration or section: math](math-mathematical-functions.md)
