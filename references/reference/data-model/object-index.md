# object.__index__(*self*)

object.__index__(*self*)

Invoked to back [`operator.index()`](https://docs.python.org/3.14/library/operator.html#operator.index), and at any point where Python must losslessly convert the numeric object into an integer object (for instance during slicing, or within the built-in [`bin()`](https://docs.python.org/3.14/library/functions.html#bin), [`hex()`](https://docs.python.org/3.14/library/functions.html#hex) and [`oct()`](https://docs.python.org/3.14/library/functions.html#oct) functions). The existence of this method signals that the numeric object is an integer type. It must return an integer.

When `__int__()`, `__float__()` and `__complex__()` are undefined, the matching built-in functions [`int()`](https://docs.python.org/3.14/library/functions.html#int), [`float()`](https://docs.python.org/3.14/library/functions.html#float) and [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) revert to `__index__()`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-numeric-types.md) · [Previous source section](object-complex-object-int-object-float.md) · [Following source section](object-round-object-trunc-object-floor-object-ceil.md)
