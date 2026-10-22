# decimal.Decimal: `number_class()`, `quantize()`, `radix()`, `remainder_near()`

number_class(*context=None*)

Yield a string that names the *class* of the operand. The value returned is one of these ten strings.

- `"-Infinity"`, indicating that the operand is negative infinity.

- `"-Normal"`, indicating that the operand is a negative normal number.

- `"-Subnormal"`, indicating that the operand is negative and subnormal.

- `"-Zero"`, indicating that the operand is a negative zero.

- `"+Zero"`, indicating that the operand is a positive zero.

- `"+Subnormal"`, indicating that the operand is positive and subnormal.

- `"+Normal"`, indicating that the operand is a positive normal number.

- `"+Infinity"`, indicating that the operand is positive infinity.

- `"NaN"`, indicating that the operand is a quiet NaN (Not a Number).

- `"sNaN"`, indicating that the operand is a signaling NaN.

 quantize(*exp*, *rounding=None*, *context=None*)

Yield a value matching the first operand once it has been rounded and given the exponent of the second operand.

```python
>>> Decimal('1.41421356').quantize(Decimal('1.000'))
Decimal('1.414')

```

In contrast to the other operations, should the coefficient length following the quantize operation exceed precision, an `InvalidOperation` gets signaled. This ensures that, barring an error condition, the quantized exponent always matches that of the right-hand operand.

Also setting it apart from other operations, quantize never signals Underflow, not even when the result turns out subnormal and inexact.

Should the second operand's exponent exceed that of the first, rounding might be required. Here the rounding mode follows the `rounding` argument when one is supplied, otherwise the supplied `context` argument; when neither argument is supplied, the rounding mode comes from the active thread's context.

An error comes back any time the resulting exponent lands above `Emax` or below `Etiny()`.

 radix()

Yield `Decimal(10)`, the radix (base) under which the `Decimal` class carries out all of its arithmetic. Provided for compatibility with the specification.

 remainder_near(*other*, *context=None*)

Yield the remainder produced by dividing *self* by *other*. It diverges from `self % other` because the remainder's sign is picked to keep its absolute value as small as possible. Stated exactly, the value returned is `self - n * other`, where `n` is the integer nearest the exact value of `self / other`, and whenever two integers sit equally near, the even one wins.

When the result equals zero, its sign becomes the sign of *self*.

```python
>>> Decimal(18).remainder_near(Decimal(10))
Decimal('-2')
>>> Decimal(25).remainder_near(Decimal(10))
Decimal('5')
>>> Decimal(35).remainder_near(Decimal(10))
Decimal('-5')

```

[Subject index](INDEX.md) · [Previous](decimal-decimal-is-subnormal-to-decimal-decimal-normalize.md) · [Continue](decimal-decimal-rotate-to-decimal-decimal-round.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Decimal](decimal-decimal-class.md) · [Owning module, declaration or section: Decimal objects](decimal-decimal-class.md)
