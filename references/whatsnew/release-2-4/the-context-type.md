# What’s New in Python 2.4 / The `Context` type — decimal

`traps` is a dictionary that dictates the response when particular error situations arise: either an exception gets raised or a value comes back. A few sample error situations include division by zero, precision loss, and overflow.

A thread-local default context can be reached through a call to `getcontext()`; adjusting this context's attributes lets you modify the default precision, rounding behavior, or trap handling. The example below demonstrates what happens when the precision of the default context is altered:

```python
>>> decimal.getcontext().prec
28
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal("0.1428571428571428571428571429")
>>> decimal.getcontext().prec = 9
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal("0.142857143")

```

You can choose how error situations are handled; the module may either hand back a special value like infinity or not-a-number, or it may raise exceptions instead:

```python
>>> decimal.Decimal(1) / decimal.Decimal(0)
Traceback (most recent call last):
  ...
decimal.DivisionByZero: x / 0
>>> decimal.getcontext().traps[decimal.DivisionByZero] = False
>>> decimal.Decimal(1) / decimal.Decimal(0)
Decimal("Infinity")
>>>

```

A `Context` instance additionally provides several number-formatting methods, among them `to_eng_string()` and `to_sci_string()`.

To learn more, consult the documentation for the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module, which provides both a quick-start tutorial and a reference.

See also

[**PEP 327**](https://peps.python.org/pep-0327/) - Decimal Data Type

Authored by Facundo Batista; the implementation came from Facundo Batista, along with Eric Price, Raymond Hettinger, Aahz, and Tim Peters.

[http://www.lahey.com/float.htm](https://web.archive.org/web/20230604072523/http://www.lahey.com/float.htm)

This article relies on Fortran code to demonstrate many of the troubles that floating-point inaccuracy is capable of producing.

[https://speleotrove.com/decimal/](https://speleotrove.com/decimal/)

An account of a decimal-based representation. The representation is being put forward as a standard, and it forms the basis of Python's new decimal type. A great deal of this content was authored by Mike Cowlishaw, the person who designed the Rexx language.

### The `Context` type

Several settings that govern decimal operations are bundled inside instances of the `Context` class:

- `prec` is the precision, the number of decimal places.

- The rounding mode gets named by `rounding`. For the assorted choices the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module defines constants: `ROUND_DOWN`, `ROUND_CEILING`, `ROUND_HALF_EVEN`, and several more.

-

[Subject index](INDEX.md) · [Next source section](pep-328-multi-line-imports.md) · [Release/subject declaration](pep-218-built-in-set-objects.md) · [Previous source section](decimal-square-roots-and-contexts.md)
