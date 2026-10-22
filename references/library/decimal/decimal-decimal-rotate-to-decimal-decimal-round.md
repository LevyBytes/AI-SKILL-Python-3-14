# decimal.Decimal: `rotate()`, `same_quantum()`, `scaleb()`, `shift()`, `sqrt()`, `to_eng_string()`, `to_integral()`, `to_integral_exact()`, `to_integral_value()`, `round()`

rotate(*other*, *context=None*)

Yield the outcome of rotating the first operand's digits by a count that the second operand fixes. That second operand has to be an integer within the range -precision through precision. The magnitude of the second operand sets how many places to rotate. A positive second operand rotates leftward; otherwise the rotation goes rightward. Where needed, the first operand's coefficient is left-padded with zeros up to length precision. The first operand's sign and exponent remain untouched.

 same_quantum(*other*, *context=None*)

Check whether self and other share the same exponent, or whether both happen to be `NaN`.

Context has no bearing on this operation and it stays quiet: no flags shift and no rounding takes place. One exception applies: the C version can raise InvalidOperation when the second operand cannot be converted exactly.

 scaleb(*other*, *context=None*)

Yield the first operand after adjusting its exponent by the second. Put another way, yield the first operand multiplied by `10**other`. That second operand has to be an integer.

 shift(*other*, *context=None*)

Yield the outcome of shifting the first operand's digits by a count that the second operand fixes. That second operand has to be an integer within the range -precision through precision. The magnitude of the second operand sets how many places to shift. A positive second operand shifts leftward; otherwise the shift goes rightward. The digits brought into the coefficient are zeros. The first operand's sign and exponent remain untouched.

 sqrt(*context=None*)

Yield the square root of the argument computed to full precision.

 to_eng_string(*context=None*)

Turn the value into a string, applying engineering notation whenever an exponent is called for.

In engineering notation the exponent is always a multiple of 3. That can leave as many as 3 digits ahead of the decimal point and may call for tacking on one or two trailing zeros.

To illustrate, this turns `Decimal('123E+1')` into `Decimal('1.23E+3')`.

 to_integral(*rounding=None*, *context=None*)

The same as the `to_integral_value()` method. The `to_integral` name has been retained for compatibility with earlier versions.

 to_integral_exact(*rounding=None*, *context=None*)

Round toward the nearest integer, signaling `Inexact` or `Rounded` as warranted whenever rounding takes place. The rounding mode follows the `rounding` parameter when supplied, otherwise the supplied `context`. When neither parameter is supplied, the rounding mode comes from the current context.

 to_integral_value(*rounding=None*, *context=None*)

Round toward the nearest integer with no signaling of `Inexact` or `Rounded`. When supplied, *rounding* is applied; otherwise the rounding method from either the supplied *context* or the current context is used.

Decimal numbers can be rounded using the [`round()`](https://docs.python.org/3.14/library/functions.html#round) function:

 round(number)

 round(number, ndigits)

When *ndigits* is omitted or `None`, yields the nearest [`int`](https://docs.python.org/3.14/library/functions.html#int) to *number*, breaking ties toward even and disregarding the rounding mode of the `Decimal` context. Raises [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) when *number* is an infinity, or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when it is a (quiet or signaling) NaN.

When *ndigits* is an [`int`](https://docs.python.org/3.14/library/functions.html#int), the context's rounding mode is honored and a `Decimal` standing for *number* rounded to the nearest multiple of `Decimal('1E-ndigits')` comes back; here `round(number, ndigits)` amounts to `self.quantize(Decimal('1E-ndigits'))`. Yields `Decimal('NaN')` when *number* is a quiet NaN. Raises `InvalidOperation` when *number* is an infinity, a signaling NaN, or when the coefficient length following the quantize operation would surpass the current context's precision. Said differently, for the non-corner cases:

- if *ndigits* is positive, return *number* rounded to *ndigits* decimal places;

- if *ndigits* is zero, return *number* rounded to the nearest integer;

- if *ndigits* is negative, return *number* rounded to the nearest multiple of `10**abs(ndigits)`.

For example:

```python
>>> from decimal import Decimal, getcontext, ROUND_DOWN
>>> getcontext().rounding = ROUND_DOWN
>>> round(Decimal('3.75'))     # context rounding ignored
4
>>> round(Decimal('3.5'))      # round-ties-to-even
4
>>> round(Decimal('3.75'), 0)  # uses the context rounding
Decimal('3')
>>> round(Decimal('3.75'), 1)
Decimal('3.7')
>>> round(Decimal('3.75'), -1)
Decimal('0E+1')

```

[Subject index](INDEX.md) · [Previous](decimal-construction-arithmetic-and-remainders.md) · [Continue](logical-operands.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Decimal](decimal-decimal-class.md) · [Owning module, declaration or section: Decimal objects](decimal-decimal-class.md)
