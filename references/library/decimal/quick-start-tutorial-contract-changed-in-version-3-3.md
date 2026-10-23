# decimal - Quick-start tutorial - Contract: Changed in version 3.3.

Changed in version 3.3.

Decimals cooperate nicely with much of the rest of Python. What follows is a brief decimal floating-point flying circus:

```pycon
>>> data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
>>> max(data)
Decimal('9.25')
>>> min(data)
Decimal('0.03')
>>> sorted(data)
[Decimal('0.03'), Decimal('1.00'), Decimal('1.34'), Decimal('1.87'),
 Decimal('2.35'), Decimal('3.45'), Decimal('9.25')]
>>> sum(data)
Decimal('19.29')
>>> a,b,c = data[:3]
>>> str(a)
'1.34'
>>> float(a)
1.34
>>> round(a, 1)
Decimal('1.3')
>>> int(a)
1
>>> a * 5
Decimal('6.70')
>>> a * b
Decimal('2.5058')
>>> c % a
Decimal('0.77')

```

You can render Decimals (via the [`format()`](https://docs.python.org/3.14/library/functions.html#format) built-in or [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings)) in either fixed-point or scientific notation, drawing on the identical formatting syntax (see [Format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec)) that the builtin [`float`](https://docs.python.org/3.14/library/functions.html#float) type uses:

```pycon
>>> format(Decimal('2.675'), "f")
'2.675'
>>> format(Decimal('2.675'), ".2f")
'2.68'
>>> f"{Decimal('2.675'):.2f}"
'2.68'
>>> format(Decimal('2.675'), ".2e")
'2.68e+0'
>>> with localcontext() as ctx:
...     ctx.rounding = ROUND_DOWN
...     print(format(Decimal('2.675'), ".2f"))
...
2.67

```

A handful of mathematical functions are likewise offered on Decimal:

```python
>>> getcontext().prec = 28
>>> Decimal(2).sqrt()
Decimal('1.414213562373095048801688724')
>>> Decimal(1).exp()
Decimal('2.718281828459045235360287471')
>>> Decimal('10').ln()
Decimal('2.302585092994045684017991455')
>>> Decimal('10').log10()
Decimal('1')

```

A number is rounded to a fixed exponent by the `quantize()` method. It comes in handy for monetary work that frequently rounds outcomes to a set number of places:

```python
>>> Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN)
Decimal('7.32')
>>> Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP)
Decimal('8')

```

As demonstrated earlier, the `getcontext()` function reaches the active context and lets its settings be modified. Most applications are well served by this method.

When the work is more involved, building separate contexts with the `Context()` constructor can help. Activate one of these by calling the `setcontext()` function.

Following the standard, the `decimal` module ships two prebuilt standard contexts, `BasicContext` and `ExtendedContext`. The first is especially handy when debugging, since a lot of the traps are switched on:

[Subject index](INDEX.md) · [Previous](decimal-quickstart-overview.md) · [Continue](decimal-context-precision-and-rounding-example.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Quick-start tutorial](decimal-quickstart-overview.md)
