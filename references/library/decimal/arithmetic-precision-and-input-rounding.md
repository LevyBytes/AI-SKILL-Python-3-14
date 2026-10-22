# Decimal arithmetic precision and input rounding

```pycon
>>> getcontext().prec = 3
>>> Decimal('3.104') + Decimal('2.104')
Decimal('5.21')
>>> Decimal('3.104') + Decimal('0.000') + Decimal('2.104')
Decimal('5.20')

```

Two remedies exist: raise the precision, or compel the inputs to round by applying the unary plus operation:

```pycon
>>> getcontext().prec = 3
>>> +Decimal('1.23456789')      # unary plus triggers rounding
Decimal('1.23')

```

As another option, the `Context.create_decimal()` method lets you round inputs at the moment they are constructed:

```python
>>> Context(prec=5, rounding=ROUND_DOWN).create_decimal('1.2345678')
Decimal('1.2345')

```

Q: Is the CPython implementation fast for large numbers?

A: Yes. Within CPython and PyPy3, the C/CFFI builds of the decimal module fold in the fast [libmpdec](https://www.bytereef.org/mpdecimal/doc/libmpdec/index.html) library, which delivers arbitrary-precision, correctly rounded decimal floating-point arithmetic [1]. For numbers of moderate size `libmpdec` turns to [Karatsuba multiplication](https://en.wikipedia.org/wiki/Karatsuba_algorithm), while for the very largest it switches to the [Number Theoretic Transform](https://en.wikipedia.org/wiki/Discrete_Fourier_transform_(general)#Number-theoretic_transform).

To do exact arbitrary-precision arithmetic, the context needs tuning. Keep `Emin` and `Emax` pinned to their maximum values, and leave `clamp` at 0, which is the default. Choosing a value for `prec`, though, calls for a bit of caution.

When you simply want to experiment with bignum arithmetic, the most painless route is to give `prec` its maximum value too [2]:

```python
>>> setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))
>>> x = Decimal(2) ** 256
>>> x / 128
Decimal('904625697166532776746648320380374280103671755200316906558262375061821325312')

```

Once results turn inexact, `MAX_PREC` becomes wildly oversized on 64-bit platforms, and there simply will not be enough memory to go around:

```python
>>> Decimal(1) / 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
MemoryError

```

Where overallocation is available (Linux being one example), a smarter tactic is to size `prec` against however much RAM is on hand. Imagine you hold 8GB of RAM and anticipate 10 simultaneous operands, each consuming at most 500MB:

```python
>>> import sys
>>>
>>> # Maximum number of digits for a single operand using 500MB in 8-byte words
>>> # with 19 digits per word (4-byte and 9 digits for the 32-bit build):
>>> maxdigits = 19 * ((500 * 1024**2) // 8)
>>>
>>> # Check that this works:
>>> c = Context(prec=maxdigits, Emax=MAX_EMAX, Emin=MIN_EMIN)
>>> c.traps[Inexact] = True
>>> setcontext(c)
>>>
>>> # Fill the available precision with nines:
>>> x = Decimal(0).logical_invert() * 9
>>> sys.getsizeof(x)
524288112
>>> x + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  decimal.Inexact: [<class 'decimal.Inexact'>]

```

As a rule — and all the more so where overallocation is absent — it pays to figure even tighter bounds and to enable the `Inexact` trap whenever every calculation is supposed to come out exact.

[Subject index](INDEX.md)
