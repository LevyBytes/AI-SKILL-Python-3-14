# Recovering the stored decimal value and exact fractions

Thus the computer never truly “sees” 1/10; what it perceives is the exact fraction shown above, the finest IEEE 754 double approximation within reach:

```pycon
>>> 0.1 * 2 ** 55
3602879701896397.0

```

Multiplying that fraction by `10**55` lets us read the value out to its 55th decimal digit:

```pycon
>>> 3602879701896397 * 10 ** 55 // 2 ** 55
1000000000000000055511151231257827021181583404541015625

```

which tells us the precise number held in the computer equals the decimal value 0.1000000000000000055511151231257827021181583404541015625. Rather than print that complete decimal, a good many languages (older Python builds included) round it off to 17 significant digits:

```pycon
>>> format(0.1, '.17f')
'0.10000000000000001'

```

Carrying out these computations is straightforward with the [`fractions`](https://docs.python.org/3.14/library/fractions.html#module-fractions) and [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) modules:

```pycon
>>> from decimal import Decimal
>>> from fractions import Fraction

>>> Fraction.from_float(0.1)
Fraction(3602879701896397, 36028797018963968)

>>> (0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)

>>> Decimal.from_float(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')

>>> format(Decimal.from_float(0.1), '.17')
'0.10000000000000001'

```

[Subject index](INDEX.md) · [Previous source section](deriving-the-nearest-binary64-representation-of-one-tenth.md) · [Related tutorial example and explanation](deriving-the-nearest-binary64-representation-of-one-tenth.md)
