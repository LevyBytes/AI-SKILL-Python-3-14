# What’s New in Python 2.4 / The `Decimal` type — cmath, decimal, math

### The `Decimal` type

A fresh module, [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal), joined Python’s standard library. Inside it sit two classes, `Decimal` and `Context`. Numbers are what `Decimal` instances stand for, while `Context` instances bundle assorted settings like the precision and the default rounding mode.

Much like ordinary Python integers and FP numbers, `Decimal` instances are immutable; after one is created, the value it stands for can’t be altered. You can build `Decimal` instances out of integers or strings:

```python
>>> import decimal
>>> decimal.Decimal(1972)
Decimal("1972")
>>> decimal.Decimal("1.1")
Decimal("1.1")

```

You can additionally supply tuples holding the sign, the mantissa given as a tuple of decimal digits, and the exponent:

```python
>>> decimal.Decimal((1, (1, 4, 7, 5), -2))
Decimal("-14.75")

```

A word of warning: since the sign bit is a Boolean, 0 means positive while 1 means negative.

Conversion from floating-point numbers raises a slight snag: ought the FP number that stands for 1.1 become the decimal for precisely 1.1, or for 1.1 together with whatever inaccuracies crept in? The choice made was to sidestep the matter and keep such a conversion out of the API. What you should do instead is render the floating-point number as a string at your chosen precision and feed that string to the `Decimal` constructor:

```python
>>> f = 1.1
>>> decimal.Decimal(str(f))
Decimal("1.1")
>>> decimal.Decimal('%.12f' % f)
Decimal("1.100000000000")

```

With `Decimal` instances in hand, you can run the usual math operations across them. One catch: exponentiation calls for an integer exponent:

```python
>>> a = decimal.Decimal('35.72')
>>> b = decimal.Decimal('1.73')
>>> a+b
Decimal("37.45")
>>> a-b
Decimal("33.99")
>>> a*b
Decimal("61.7956")
>>> a/b
Decimal("20.64739884393063583815028902")
>>> a ** 2
Decimal("1275.9184")
>>> a**b
Traceback (most recent call last):
  ...
decimal.InvalidOperation: x ** (non-integer)

```

It’s fine to mix `Decimal` instances with integers, though not with floating-point numbers:

```python
>>> a + 4
Decimal("39.72")
>>> a + 4.5
Traceback (most recent call last):
  ...
TypeError: You can interact Decimal only with int, long or Decimal data types.
>>>

```

Although `Decimal` numbers work alongside the [`math`](https://docs.python.org/3.14/library/math.html#module-math) and [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) modules, be aware that they get converted to floating-point numbers right away before the operation runs, which can cost you precision and accuracy. What comes back, too, is an ordinary floating-point number rather than a `Decimal`.

```python
>>> import math, cmath
>>> d = decimal.Decimal('123456789012.345')
>>> math.sqrt(d)
351364.18288201344
>>> cmath.sqrt(-d)
351364.18288201344j

```

[Subject index](INDEX.md) · [Previous source section](why-is-decimal-needed.md) · [Next source section](decimal-square-roots-and-contexts.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
