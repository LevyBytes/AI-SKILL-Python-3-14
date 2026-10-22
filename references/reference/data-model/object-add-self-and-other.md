# object.__add__(*self*, *other*) / object.__sub__(*self*, *other*) / object.__mul__(*self*, *other*) / object.__matmul__(*self*, *other*) / object.__truediv__(*self*, *other*) / object.__floordiv__(*self*, *other*) / object.__mod__(*self*, *other*) / object.__divmod__(*self*, *other*) / object.__pow__(*self*, *other*[, *modulo*]) / object.__lshift__(*self*, *other*) / object.__rshift__(*self*, *other*) / object.__and__(*self*, *other*) / object.__xor__(*self*, *other*) / object.__or__(*self*, *other*)

object.__add__(*self*, *other*)

 object.__sub__(*self*, *other*)

 object.__mul__(*self*, *other*)

 object.__matmul__(*self*, *other*)

 object.__truediv__(*self*, *other*)

 object.__floordiv__(*self*, *other*)

 object.__mod__(*self*, *other*)

 object.__divmod__(*self*, *other*)

 object.__pow__(*self*, *other*[, *modulo*])

 object.__lshift__(*self*, *other*)

 object.__rshift__(*self*, *other*)

 object.__and__(*self*, *other*)

 object.__xor__(*self*, *other*)

 object.__or__(*self*, *other*)

These methods run to back the binary arithmetic operations (`+`, `-`, `*`, `@`, `/`, `//`, `%`, [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod), [`pow()`](https://docs.python.org/3.14/library/functions.html#pow), `**`, `<<`, `>>`, `&`, `^`, `|`). For example, to compute the expression `x + y`, where *x* is an instance of a class providing an `__add__()` method, `type(x).__add__(x, y)` gets called. The `__divmod__()` method ought to be the equivalent of combining `__floordiv__()` and `__mod__()`; it should bear no relation to `__truediv__()`. Be aware that `__pow__()` should be defined to take an optional third argument when support for the three-argument form of the built-in `pow()` function is desired.

When one of these methods cannot perform the operation with the given arguments, it should return [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-numeric-types.md) · [Previous source section](emulating-numeric-types.md) · [Following source section](object-radd-self-and-other.md)
