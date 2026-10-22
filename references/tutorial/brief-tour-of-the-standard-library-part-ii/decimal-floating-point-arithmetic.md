# 11.8. Decimal floating-point arithmetic

### 11.8. Decimal floating-point arithmetic

A [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) datatype for decimal floating-point arithmetic is provided by the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module. Measured against the built-in [`float`](https://docs.python.org/3.14/library/functions.html#float) implementation of binary floating point, this class earns its keep in particular for

- financial applications and other uses which require exact decimal representation,

- control over precision,

- control over rounding to meet legal or regulatory requirements,

- tracking of significant decimal places, or

- uses in which the user anticipates that results will line up with figures worked out by hand.

Take, for instance, working out a 5% tax on a 70 cent phone charge: decimal floating point and binary floating point yield different answers. Once you round the outcomes to the nearest cent, that gap turns out to matter:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73

```

That [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) outcome retains a trailing zero, deducing four-place significance on its own from multiplicands carrying two-place significance. Decimal mirrors arithmetic the way it's done by hand and sidesteps the trouble that crops up when binary floating point can't represent decimal amounts exactly.

Because its representation is exact, the [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) class can carry out modulo operations and equality checks that aren't dependable in binary floating point:

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False

```

You can dial up as much precision as a task demands with the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')

```

[Subject index](INDEX.md) · [Previous source section](tools-for-working-with-lists.md) · [Following source section](../virtual-environments-and-packages/introduction.md)
