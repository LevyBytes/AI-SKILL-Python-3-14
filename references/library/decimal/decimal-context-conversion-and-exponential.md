# decimal.Context: Decimal context conversion, arithmetic and comparisons

create_decimal_from_float(*f*, */*)

Builds a fresh Decimal instance out of a float *f* while rounding under *self* as the context. In contrast to the `Decimal.from_float()` class method, the context precision, rounding method, flags, and traps all apply to the conversion.

```pycon
>>> context = Context(prec=5, rounding=ROUND_DOWN)
>>> context.create_decimal_from_float(math.pi)
Decimal('3.1415')
>>> context = Context(prec=5, traps=[Inexact])
>>> context.create_decimal_from_float(math.pi)
Traceback (most recent call last):
    ...
decimal.Inexact: None

```

Added in version 3.1.

 Etiny()

Yields a value equal to `Emin - prec + 1`, which marks the minimum exponent value for subnormal results. Once underflow happens, the exponent is set to `Etiny`.

 Etop()

Yields a value equal to `Emax - prec + 1`.

The customary way of working with decimals is to build `Decimal` instances and then run arithmetic operations on them, which happen inside the active thread's current context. Another way is to call context methods so the calculation stays within a particular context. These methods resemble those of the `Decimal` class and are recapped here only in brief.

 abs(*x*, */*)

Returns the absolute value of *x*.

 add(*x*, *y*, */*)

Return the sum of *x* and *y*.

 canonical(*x*, */*)

Returns the same Decimal object *x*.

 compare(*x*, *y*, */*)

Compares *x* and *y* numerically.

 compare_signal(*x*, *y*, */*)

Compares the values of the two operands numerically.

 compare_total(*x*, *y*, */*)

Compares two operands using their abstract representation.

 compare_total_mag(*x*, *y*, */*)

Compares two operands using their abstract representation, ignoring sign.

 copy_abs(*x*, */*)

Returns a copy of *x* with the sign set to 0.

 copy_negate(*x*, */*)

Returns a copy of *x* with the sign inverted.

 copy_sign(*x*, *y*, */*)

Copies the sign from *y* to *x*.

 divide(*x*, *y*, */*)

Return *x* divided by *y*.

 divide_int(*x*, *y*, */*)

Return *x* divided by *y*, truncated to an integer.

 divmod(*x*, *y*, */*)

Divides two numbers and returns the integer part of the result.

 exp(*x*, */*)

Returns `e ** x`.

[Subject index](INDEX.md) · [Previous](decimal-context-class-to-decimal-context-create-decimal.md) · [Continue](decimal-context-fma-to-decimal-context-min.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Context](decimal-context-class-to-decimal-context-create-decimal.md) · [Owning module, declaration or section: Context objects](decimal-getcontext-to-decimal-defaultcontext.md)
