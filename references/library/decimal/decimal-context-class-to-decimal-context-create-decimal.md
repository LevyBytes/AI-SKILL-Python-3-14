# decimal / Context objects: `decimal.Context`, `clear_flags()`, `clear_traps()`, `copy()`, `copy_decimal()`, `create_decimal()`

*class *decimal.Context(*prec=None*, *rounding=None*, *Emin=None*, *Emax=None*, *capitals=None*, *clamp=None*, *flags=None*, *traps=None*)

Builds a fresh context. When a field goes unspecified or is [`None`](https://docs.python.org/3.14/library/constants.html#None), its default value is taken from the `DefaultContext`. When the *flags* field goes unspecified or is `None`, every flag starts cleared.

 prec

An integer within the range [`1`, `MAX_PREC`] that fixes the precision used by arithmetic operations in the context.

 rounding

One among the constants enumerated in the section Rounding Modes.

 traps

 flags

Lists of whichever signals should be set. As a rule, fresh contexts ought to set only traps and keep the flags clear.

 Emin

 Emax

Integers that fix the outer bounds permitted for exponents. *Emin* has to fall within the range [`MIN_EMIN`, `0`], and *Emax* within the range [`0`, `MAX_EMAX`].

 capitals

Either `0` or `1` (the default). When set to `1`, exponents print with a capital `E`; otherwise a lowercase `e` appears: `Decimal('6.02e+23')`.

 clamp

Either `0` (the default) or `1`. When set to `1`, the exponent `e` of a `Decimal` instance representable in this context is held strictly inside the range `Emin - prec + 1 <= e <= Emax - prec + 1`. When *clamp* is `0` a looser condition applies: the adjusted exponent of the `Decimal` instance stays at most `Emax`. With *clamp* set to `1`, a large normal number will, wherever it can, have its exponent lowered and a matching count of zeros appended to its coefficient, so as to satisfy the exponent constraints; this keeps the number's value while discarding information about significant trailing zeros. For example:

```python
>>> Context(prec=6, Emax=999, clamp=1).create_decimal('1.23e999')
Decimal('1.23000E+999')

```

A *clamp* value of `1` enables compatibility with the fixed-width decimal interchange formats laid out in IEEE 754.

The `Context` class supplies several general purpose methods together with a sizable set of methods for performing arithmetic right inside a given context. Moreover, every one of the `Decimal` methods covered above (save for the `adjusted()` and `as_tuple()` methods) has a matching `Context` method. For instance, given a `Context` instance `C` and a `Decimal` instance `x`, `C.exp(x)` is the same as `x.exp(context=C)`. Each `Context` method takes a Python integer (an instance of [`int`](https://docs.python.org/3.14/library/functions.html#int)) wherever a Decimal instance is taken.

 clear_flags()

Resets all of the flags to `0`.

 clear_traps()

Resets all of the traps to `0`.

Added in version 3.3.

 copy()

Yield a duplicate of the context.

 copy_decimal(*num*, */*)

Yield a copy of the Decimal instance num.

 create_decimal(*num='0'*, */*)

Builds a fresh Decimal instance out of *num* while drawing on *self* as the context. In contrast to the `Decimal` constructor, the context precision, rounding method, flags, and traps all apply to the conversion.

This proves handy because constants tend to be supplied at a higher precision than the application actually needs. A further upside is that rounding right away clears away unintended effects from digits past the current precision. In the example that follows, feeding in unrounded inputs means that adding zero to a sum can alter the result:

```pycon
>>> getcontext().prec = 3
>>> Decimal('3.4445') + Decimal('1.0023')
Decimal('4.45')
>>> Decimal('3.4445') + Decimal(0) + Decimal('1.0023')
Decimal('4.44')

```

This method realizes the to-number operation of the IBM specification. Should you pass a string, it must carry no surrounding whitespace and no underscores at either end.

[Subject index](INDEX.md) · [Previous](decimal-getcontext-to-decimal-defaultcontext.md) · [Continue](decimal-context-conversion-and-exponential.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Context objects](decimal-getcontext-to-decimal-defaultcontext.md)
