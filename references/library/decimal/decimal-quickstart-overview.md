# decimal - Quick-start tutorial - Section introduction and initial examples

### Quick-start tutorial

Working with decimals normally begins by importing the module, inspecting the present context through `getcontext()`, and — when required — assigning fresh values for precision, rounding, or active traps:

```python
>>> from decimal import *
>>> getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])

>>> getcontext().prec = 7       # Set a new precision

```

You can build Decimal instances from integers, strings, floats, or tuples. Building from an integer or float converts that integer's or float's value exactly. Among Decimal numbers are special values like `NaN`, short for “Not a number”, both signs of `Infinity`, and `-0`:

```python
>>> getcontext().prec = 28
>>> Decimal(10)
Decimal('10')
>>> Decimal('3.14')
Decimal('3.14')
>>> Decimal(3.14)
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> Decimal((0, (3, 1, 4), -2))
Decimal('3.14')
>>> Decimal(str(2.0 ** 0.5))
Decimal('1.4142135623730951')
>>> Decimal(2) ** Decimal('0.5')
Decimal('1.414213562373095048801688724')
>>> Decimal('NaN')
Decimal('NaN')
>>> Decimal('-Infinity')
Decimal('-Infinity')

```

When the `FloatOperation` signal is trapped, inadvertently combining decimals with floats inside constructors or ordering comparisons triggers an exception:

```python
>>> c = getcontext()
>>> c.traps[FloatOperation] = True
>>> Decimal(3.14)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
>>> Decimal('3.5') < 3.7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
>>> Decimal('3.5') == 3.5
True

```

Added in version 3.3.

How significant a freshly made Decimal is depends only on how many digits were supplied. Context precision and rounding take effect exclusively during arithmetic.

```pycon
>>> getcontext().prec = 6
>>> Decimal('3.0')
Decimal('3.0')
>>> Decimal('3.1415926535')
Decimal('3.1415926535')
>>> Decimal('3.1415926535') + Decimal('2.7182818285')
Decimal('5.85987')
>>> getcontext().rounding = ROUND_UP
>>> Decimal('3.1415926535') + Decimal('2.7182818285')
Decimal('5.85988')

```

Should the C version's internal limits be surpassed, building a decimal raises `InvalidOperation`:

```python
>>> Decimal("1e9999999999999999999")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]

```

[Subject index](INDEX.md) · [Previous](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Continue](quick-start-tutorial-contract-changed-in-version-3-3.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)
