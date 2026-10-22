# decimal.Decimal: `adjusted()`, `as_integer_ratio()`, `as_tuple()`, `canonical()`, `compare()`, `compare_signal()`, `compare_total()`, `compare_total_mag()`, `conjugate()`, `copy_abs()`, `copy_negate()`

adjusted()

Return the adjusted exponent obtained by pushing out the coefficient’s rightmost digits until just the lead digit is left: `Decimal('321e+5').adjusted()` gives seven. This serves to locate where the most significant digit sits relative to the decimal point.

 as_integer_ratio()

Return an integer pair `(n, d)` expressing the supplied `Decimal` instance as a fraction reduced to lowest terms and bearing a positive denominator:

```python
>>> Decimal('-3.14').as_integer_ratio()
(-157, 50)

```

This conversion is exact. Raise OverflowError on infinities and ValueError on NaNs.

Added in version 3.6.

 as_tuple()

Return a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) representation of the number: `DecimalTuple(sign, digits, exponent)`.

 canonical()

Return the canonical encoding of the argument. At present a `Decimal` instance's encoding is always canonical, so this operation returns its argument unchanged.

 compare(*other*, *context=None*)

Compare the values of two Decimal instances. `compare()` returns a Decimal instance, and should either operand be a NaN then a NaN is the result:

```python
a or b is a NaN  ==> Decimal('NaN')
a < b            ==> Decimal('-1')
a == b           ==> Decimal('0')
a > b            ==> Decimal('1')

```

 compare_signal(*other*, *context=None*)

This operation matches the `compare()` method exactly, save that all NaNs signal. Put differently, provided neither operand is a signaling NaN, any quiet NaN operand is handled as if it were a signaling NaN.

 compare_total(*other*, *context=None*)

Compare two operands by their abstract representation instead of their numeric value. Resembling the `compare()` method, but here the result yields a total ordering over `Decimal` instances. Two `Decimal` instances sharing the same numeric value yet differing in representation compare unequal under this ordering:

```python
>>> Decimal('12.0').compare_total(Decimal('12'))
Decimal('-1')

```

Quiet and signaling NaNs take part in the total ordering as well. This function's result is `Decimal('0')` when both operands carry the same representation, `Decimal('-1')` when the first operand sits below the second in the total order, and `Decimal('1')` when the first operand sits above the second operand. Consult the specification for the total order's particulars.

Context does not affect this operation, and it is quiet: no flags change and no rounding takes place. By way of exception, the C version may raise InvalidOperation when the second operand cannot be converted exactly.

 compare_total_mag(*other*, *context=None*)

Compare two operands by their abstract representation rather than their value, as with `compare_total()`, except the sign of each operand is disregarded. `x.compare_total_mag(y)` is equivalent to `x.copy_abs().compare_total(y.copy_abs())`.

Context does not affect this operation, and it is quiet: no flags change and no rounding takes place. By way of exception, the C version may raise InvalidOperation when the second operand cannot be converted exactly.

 conjugate()

Just returns self; this method exists solely to satisfy the Decimal Specification.

 copy_abs()

Return the absolute value of the argument. The context does not affect this operation, and it is quiet: no flags change and no rounding takes place.

 copy_negate()

Return the negation of the argument. The context does not affect this operation, and it is quiet: no flags change and no rounding takes place.

[Subject index](INDEX.md) · [Previous](decimal-decimal-class.md) · [Continue](decimal-decimal-copy-sign-to-decimal-decimal-is-finite.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Decimal](decimal-decimal-class.md) · [Owning module, declaration or section: Decimal objects](decimal-decimal-class.md)
