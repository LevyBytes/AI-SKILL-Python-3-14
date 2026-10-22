# decimal.Decimal: `copy_sign()`, `exp()`, `from_float()`, `from_number()`, `fma()`, `is_canonical()`, `is_finite()`

copy_sign(*other*, *context=None*)

Return a copy of the first operand whose sign is set to match the second operand's sign. As an example:

```python
>>> Decimal('2.3').copy_sign(Decimal('-1.5'))
Decimal('-2.3')

```

Context does not affect this operation, and it is quiet: no flags change and no rounding takes place. By way of exception, the C version may raise InvalidOperation when the second operand cannot be converted exactly.

 exp(*context=None*)

Return, evaluated at the supplied number, the value of the (natural) exponential function `e**x`. That result is correctly rounded under the `ROUND_HALF_EVEN` rounding mode.

```python
>>> Decimal(1).exp()
Decimal('2.718281828459045235360287471')
>>> Decimal(321).exp()
Decimal('2.561702493119680037517373933E+139')

```

 *classmethod *from_float(*f*, */*)

A secondary constructor whose only accepted arguments are instances of [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`int`](https://docs.python.org/3.14/library/functions.html#int).

Note `Decimal.from_float(0.1)` is not the same as `Decimal('0.1')`. Because 0.1 has no exact binary floating-point representation, it is held as the closest representable value, namely `0x1.999999999999ap-4`. The decimal equivalent of that value is `0.1000000000000000055511151231257827021181583404541015625`.

Note

Beginning with Python 3.2, you can also build a `Decimal` instance straight from a [`float`](https://docs.python.org/3.14/library/functions.html#float).

```pycon
>>> Decimal.from_float(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> Decimal.from_float(float('nan'))
Decimal('NaN')
>>> Decimal.from_float(float('inf'))
Decimal('Infinity')
>>> Decimal.from_float(float('-inf'))
Decimal('-Infinity')

```

Added in version 3.1.

 *classmethod *from_number(*number*, */*)

A secondary constructor that takes only instances of [`float`](https://docs.python.org/3.14/library/functions.html#float), [`int`](https://docs.python.org/3.14/library/functions.html#int) or `Decimal` — strings and tuples are rejected.

```pycon
>>> Decimal.from_number(314)
Decimal('314')
>>> Decimal.from_number(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> Decimal.from_number(Decimal('3.14'))
Decimal('3.14')

```

Added in version 3.14.

 fma(*other*, *third*, *context=None*)

Fused multiply-add. Return self*other+third while leaving the intermediate product self*other unrounded.

```python
>>> Decimal(2).fma(3, 5)
Decimal('11')

```

 is_canonical()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) if the argument is canonical and [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise. At present a `Decimal` instance is always canonical, so this operation always returns `True`.

 is_finite()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) when the argument is a finite number; return [`False`](https://docs.python.org/3.14/library/constants.html#False) when it is an infinity or a NaN.

[Subject index](INDEX.md) · [Previous](decimal-decimal-adjusted-to-decimal-decimal-copy-negate.md) · [Continue](decimal-decimal-is-infinite-to-decimal-decimal-is-snan.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Decimal](decimal-decimal-class.md) · [Owning module, declaration or section: Decimal objects](decimal-decimal-class.md)
