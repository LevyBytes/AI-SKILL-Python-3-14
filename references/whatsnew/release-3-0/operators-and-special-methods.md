# What's New In Python 3.0 / Operators And Special Methods

### Miscellaneous Other Changes

### Operators And Special Methods

- `!=` now returns the opposite of `==`, unless `==` returns [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented).

- “Unbound methods” are no longer a notion the language carries. Look up a method via a class attribute today and what comes back is an ordinary function object.

- The methods `__getslice__()`, `__setslice__()`, and `__delslice__()` were dropped entirely. Writing `a[i:j]` is now interpreted as `a.__getitem__(slice(i, j))` (or as [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) / [`__delitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delitem__) instead, according to whether it serves as an assignment or a deletion target).

- [**PEP 3114**](https://peps.python.org/pep-3114/): the conventional [`next()`](https://docs.python.org/3.14/library/functions.html#next) method now goes by the name [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__).

- Gone are the `__oct__()` and `__hex__()` special methods — these days [`oct()`](https://docs.python.org/3.14/library/functions.html#oct) and [`hex()`](https://docs.python.org/3.14/library/functions.html#hex) lean on [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) to turn their argument into an integer.

- Removed support for `__members__` and `__methods__`.

- Function attributes carrying the `func_X` naming were switched over to the `__X__` style, which clears those labels out of the function-attribute namespace so user-defined attributes can claim them. Specifically, `func_closure`, `func_code`, `func_defaults`, `func_dict`, `func_doc`, `func_globals`, `func_name` became, in order, [`__closure__`](https://docs.python.org/3.14/reference/datamodel.html#function.__closure__), [`__code__`](https://docs.python.org/3.14/reference/datamodel.html#function.__code__), [`__defaults__`](https://docs.python.org/3.14/reference/datamodel.html#function.__defaults__), [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#function.__dict__), [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__), [`__globals__`](https://docs.python.org/3.14/reference/datamodel.html#function.__globals__), and [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__).

- `__nonzero__()` is now [`__bool__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__bool__).

[Subject index](INDEX.md) · [Previous source section](changes-to-exceptions.md) · [Next source section](builtins.md) · [Release/subject declaration](common-stumbling-blocks.md)
