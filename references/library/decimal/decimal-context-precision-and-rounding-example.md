# decimal - Quick-start tutorial - Code example: >>> myothercontext = Context(prec=60, rounding=ROUND_HALF_DOWN)

```pycon
>>> myothercontext = Context(prec=60, rounding=ROUND_HALF_DOWN)
>>> setcontext(myothercontext)
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857142857142857142857142857')

>>> ExtendedContext
Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[])
>>> setcontext(ExtendedContext)
>>> Decimal(1) / Decimal(7)
Decimal('0.142857143')
>>> Decimal(42) / Decimal(0)
Decimal('Infinity')

>>> setcontext(BasicContext)
>>> Decimal(42) / Decimal(0)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in -toplevel-
    Decimal(42) / Decimal(0)
DivisionByZero: x / 0

```

Contexts additionally carry signal flags that track exceptional conditions met during computation. Since the flags stay set until you clear them deliberately, clearing them ahead of each batch of monitored computations — by calling the `clear_flags()` method — is the recommended practice.

```python
>>> setcontext(ExtendedContext)
>>> getcontext().clear_flags()
>>> Decimal(355) / Decimal(113)
Decimal('3.14159292')
>>> getcontext()
Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[])

```

The *flags* entry reveals that the rational approximation of pi underwent rounding (digits past the context precision were dropped) and that the outcome is inexact (a few of the dropped digits were not zero).

You assign individual traps through the dictionary held in a context's `traps` attribute:

```pycon
>>> setcontext(ExtendedContext)
>>> Decimal(1) / Decimal(0)
Decimal('Infinity')
>>> getcontext().traps[DivisionByZero] = 1
>>> Decimal(1) / Decimal(0)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in -toplevel-
    Decimal(1) / Decimal(0)
DivisionByZero: x / 0

```

The majority of programs tweak the active context just once, right at startup. And in plenty of applications, data gets turned into `Decimal` with one cast inside a loop. Once the context is established and the decimals exist, the rest of the program handles the data just as it would any other Python numeric type.

[Subject index](INDEX.md) · [Previous](quick-start-tutorial-contract-changed-in-version-3-3.md) · [Continue](decimal-decimal-class.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Quick-start tutorial](decimal-quickstart-overview.md)
