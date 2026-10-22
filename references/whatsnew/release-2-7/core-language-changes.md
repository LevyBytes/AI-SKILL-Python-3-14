# What’s New in Python 2.7 / Other Language Changes — decimal, json, marshal, pickle, sys

### Other Language Changes

A handful of more modest tweaks landed in the core language itself:

- Set-literal syntax has been pulled back from Python 3.x. The members of the new mutable set are wrapped in curly braces; what separates a set literal from a dictionary is the absence of colons and paired values. An empty `{}` still denotes an empty dictionary, so reach for `set()` whenever you want an empty set.

```pycon
>>> {1, 2, 3, 4, 5}
set([1, 2, 3, 4, 5])
>>> set() # empty set
set([])
>>> {}    # empty dict
{}

```

The back-port here was done by Alexandre Vassalotti; [bpo-2335](https://bugs.python.org/issue?@action=redirect&bpo=2335).

- Comprehensions for dictionaries and sets are a further import from 3.x, extending the list and generator comprehension idea so the literal notation for sets and dicts can be used inside it.

```pycon
>>> {x: x*x for x in range(6)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> {('a'*x) for x in range(6)}
set(['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa'])

```

Alexandre Vassalotti handled this back-port too; [bpo-2333](https://bugs.python.org/issue?@action=redirect&bpo=2333).

- A single [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement is now allowed to drive several context managers at once. They run in order from leftmost to rightmost, with each one acting as though it opened a fresh `with` block. So this:

```python
with A() as a, B() as b:
    ... suite of statements ...

```

behaves the same way as:

```python
with A() as a:
    with B() as b:
        ... suite of statements ...

```

Because `contextlib.nested()` does almost exactly the same job, it is now redundant and has been marked deprecated.

(The proposal lives at [https://codereview.appspot.com/53094](https://codereview.appspot.com/53094); Georg Brandl wrote the implementation.)

- On the great majority of platforms, going between floating-point values and strings is now rounded correctly. Such conversions crop up all over the place: when [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) is applied to floats and complex numbers; in the [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`complex`](https://docs.python.org/3.14/library/functions.html#complex) constructors; while formatting numbers; when floats and complex numbers are saved and reloaded through the [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal), [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and [`json`](https://docs.python.org/3.14/library/json.html#module-json) modules; while Python source with float and imaginary literals is parsed; and during [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)-to-float conversion.

In the same vein, the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) of a floating-point value *x* now hands back the shortest decimal string that, under correct rounding (using round-half-to-even mode), is certain to round straight back to *x*. The old behavior produced a string from rounding x out to 17 decimal digits.

The rounding code behind this works on Windows and on Unix systems built with the gcc, icc, or suncc compilers. A handful of platforms might not be able to run it correctly, and on those the code is left disabled. To see which path is active, inspect [`sys.float_repr_style`](https://docs.python.org/3.14/library/sys.html#sys.float_repr_style): it reads `short` when the new code is active and `legacy` otherwise.

The work was done by Eric Smith and Mark Dickinson, building on David Gay's `dtoa.c` library; [bpo-7117](https://bugs.python.org/issue?@action=redirect&bpo=7117).

- Turning long integers and ordinary integers into floats now rounds in a different way, picking whichever floating-point value sits nearest to the original. For small integers that translate exactly this changes nothing, but with very large numbers that must shed precision, Python 2.7 lands closer to the mark. As an illustration, here is what Python 2.6 produced:

```python
>>> n = 295147905179352891391
>>> float(n)
2.9514790517935283e+20
>>> n - long(float(n))
65535L

```

The figure Python 2.7 returns is bigger, yet far nearer the actual value:

[Subject index](INDEX.md) · [Previous source section](pep-3137-the-memoryview-object.md) · [Next source section](numeric-precision-and-format-field-changes.md) · [Release/subject declaration](the-future-for-python-2-x.md)
