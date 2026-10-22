# Numeric Types — `int`, `float`, `complex`

### Numeric Types — [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`complex`](https://docs.python.org/3.14/library/functions.html#complex)

Three separate numeric types exist: *integers*, *floating-point numbers*, and *complex numbers*. On top of that, Booleans form a subtype of integers. Precision is unlimited for integers. Floating-point numbers normally rely on double in C for their implementation; details on the precision and internal layout of floating-point numbers on whatever machine runs your program can be found in [`sys.float_info`](https://docs.python.org/3.14/library/sys.html#sys.float_info). A complex number carries a real and an imaginary part, both of them floating-point numbers. You pull these parts out of a complex number *z* with `z.real` and `z.imag`. (Two further numeric types come with the standard library: [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) for rationals, and [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) for floating-point numbers whose precision you set yourself.)

You make numbers either with numeric literals or as the output of built-in functions and operators. Plain integer literals (hex, octal and binary forms included) give you integers. A numeric literal carrying a decimal point or an exponent sign gives you a floating-point number. Tacking `'j'` or `'J'` onto a numeric literal gives you an imaginary number (a complex number whose real part is zero), which you can add to an integer or float to produce a complex number having both real and imaginary parts.

To build numbers of one particular type, use the constructors [`int()`](https://docs.python.org/3.14/library/functions.html#int), [`float()`](https://docs.python.org/3.14/library/functions.html#float), and [`complex()`](https://docs.python.org/3.14/library/functions.html#complex).

Mixed arithmetic is fully supported in Python: where a binary arithmetic operator gets operands of differing built-in numeric types, the one whose type is “narrower” is widened to match the other:

- If both arguments are complex numbers, no conversion is performed;

- should one argument be a complex or a floating-point number, then its counterpart becomes a floating-point number;

- otherwise, both must be integers and no conversion is necessary.

The standard mathematical formula governs arithmetic mixing complex and real operands, for instance:

```python
x + complex(u, v) = complex(x + u, v)
x * complex(u, v) = complex(x * u, x * v)

```

Comparing numbers of differing types acts as though the precise values of those numbers were what gets compared. [2]

Every numeric type apart from complex provides the operations below (for the priorities of these operations, refer to [Operator precedence](https://docs.python.org/3.14/reference/expressions.html#operator-summary)):

| Operation | Result | Notes | Full documentation |
| --- | --- | --- | --- |
| `x + y` | sum of *x* and *y* |  |  |
| `x - y` | difference of *x* and *y* |  |  |
| `x * y` | product of *x* and *y* |  |  |
| `x / y` | quotient of *x* and *y* |  |  |
| `x // y` | floored quotient of *x* and *y* | (1)(2) |  |
| `x % y` | remainder of `x / y` | (2) |  |
| `-x` | *x* negated |  |  |
| `+x` | *x* unchanged |  |  |
| `abs(x)` | absolute value or magnitude of *x* |  | `abs()` |
| `int(x)` | *x* converted to integer | (3)(6) | `int()` |
| `float(x)` | *x* converted to floating point | (4)(6) | `float()` |
| `complex(re, im)` | a complex number whose real part is *re* and whose imaginary part is *im*; *im* defaults to zero. | (6) | `complex()` |
| `c.conjugate()` | conjugate of the complex number *c* |  |  |
| `divmod(x, y)` | the pair `(x // y, x % y)` | (2) | `divmod()` |
| `pow(x, y)` | *x* to the power *y* | (5) | `pow()` |
| `x ** y` | *x* to the power *y* | (5) |  |

Notes:

1.

This goes by the name integer division too. With operands of type [`int`](https://docs.python.org/3.14/library/functions.html#int), the result is of type `int`. With operands of type [`float`](https://docs.python.org/3.14/library/functions.html#float), the result is of type `float`. As a rule the outcome is a whole integer, even though its type need not be `int`. Rounding always goes toward minus infinity: `1//2` is `0`, `(-1)//2` is `-1`, `1//(-2)` is `-1`, and `(-1)//(-2)` is `0`.

2.

Not for complex numbers. Instead convert to floats using [`abs()`](https://docs.python.org/3.14/library/functions.html#abs) if appropriate.

3.

Converting from [`float`](https://docs.python.org/3.14/library/functions.html#float) to [`int`](https://docs.python.org/3.14/library/functions.html#int) truncates by dropping the fractional part. For alternative conversions, see the functions [`math.floor()`](https://docs.python.org/3.14/library/math.html#math.floor) and [`math.ceil()`](https://docs.python.org/3.14/library/math.html#math.ceil).

4.

float likewise takes the strings “nan” and “inf”, optionally prefixed with “+” or “-”, for Not a Number (NaN) and for positive or negative infinity.

5.

Python sets `pow(0, 0)` and `0 ** 0` equal to `1`, as programming languages commonly do.

6.

Among the numeric literals accepted are the digits `0` to `9` together with any Unicode equivalent (code points carrying the `Nd` property).

For the full set of code points bearing the `Nd` property, consult [the Unicode Standard](https://unicode.org/Public/UNIDATA/extracted/DerivedNumericType.txt).

The whole family of [`numbers.Real`](https://docs.python.org/3.14/library/numbers.html#numbers.Real) types ([`int`](https://docs.python.org/3.14/library/functions.html#int) and [`float`](https://docs.python.org/3.14/library/functions.html#float)) additionally provides these operations:

| Operation | Result |
| --- | --- |
| `math.trunc(x)` | *x* truncated to `Integral` |
| `round(x[, n])` | *x* rounded to *n* digits, with halves rounded toward even. Leaving *n* off makes it default to 0. |
| `math.floor(x)` | the greatest `Integral` <= *x* |
| `math.ceil(x)` | the least `Integral` >= *x* |

For more numeric operations, see the [`math`](https://docs.python.org/3.14/library/math.html#module-math) and [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) modules.

[Subject index](INDEX.md) · [Previous](comparisons.md) · [Continue](bitwise-operations-on-integer-types.md)
