# decimal — Mitigating round-off error with increased precision

### Floating-point notes

### Mitigating round-off error with increased precision

Relying on decimal floating point removes decimal representation error (which is what lets `0.1` be represented exactly); even so, certain operations can still pick up round-off error once non-zero digits run past the fixed precision.

Round-off error's effects can grow when you add or subtract quantities that nearly cancel, producing loss of significance. Knuth offers two telling examples in which rounded floating-point arithmetic at insufficient precision breaks down the associative and distributive properties of addition:

```pycon
# Examples from Seminumerical Algorithms, Section 4.2.2.
>>> from decimal import Decimal, getcontext
>>> getcontext().prec = 8

>>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
>>> (u + v) + w
Decimal('9.5111111')
>>> u + (v + w)
Decimal('10')

>>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
>>> (u*v) + (u*w)
Decimal('0.01')
>>> u * (v+w)
Decimal('0.0060000')

```

The `decimal` module lets you recover these identities by widening the precision enough to sidestep loss of significance:

```pycon
>>> getcontext().prec = 20
>>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
>>> (u + v) + w
Decimal('9.51111111')
>>> u + (v + w)
Decimal('9.51111111')
>>>
>>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
>>> (u*v) + (u*w)
Decimal('0.0060000')
>>> u * (v+w)
Decimal('0.0060000')

```

[Subject index](INDEX.md) · [Continue](special-values.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)
