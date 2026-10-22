# object.__radd__(*self*, *other*) / object.__rsub__(*self*, *other*) / object.__rmul__(*self*, *other*) / object.__rmatmul__(*self*, *other*) / object.__rtruediv__(*self*, *other*) / object.__rfloordiv__(*self*, *other*) / object.__rmod__(*self*, *other*) / object.__rdivmod__(*self*, *other*) / object.__rpow__(*self*, *other*[, *modulo*]) / object.__rlshift__(*self*, *other*) / object.__rrshift__(*self*, *other*) / object.__rand__(*self*, *other*) / object.__rxor__(*self*, *other*) / object.__ror__(*self*, *other*)

object.__radd__(*self*, *other*)

 object.__rsub__(*self*, *other*)

 object.__rmul__(*self*, *other*)

 object.__rmatmul__(*self*, *other*)

 object.__rtruediv__(*self*, *other*)

 object.__rfloordiv__(*self*, *other*)

 object.__rmod__(*self*, *other*)

 object.__rdivmod__(*self*, *other*)

 object.__rpow__(*self*, *other*[, *modulo*])

 object.__rlshift__(*self*, *other*)

 object.__rrshift__(*self*, *other*)

 object.__rand__(*self*, *other*)

 object.__rxor__(*self*, *other*)

 object.__ror__(*self*, *other*)

These methods run to back the binary arithmetic operations (`+`, `-`, `*`, `@`, `/`, `//`, `%`, [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod), [`pow()`](https://docs.python.org/3.14/library/functions.html#pow), `**`, `<<`, `>>`, `&`, `^`, `|`) using reflected (swapped) operands. These functions run only when the operands have different types, when the left operand lacks support for the matching operation [3], or when the right operand's class descends from the left operand's class. [4] For example, to compute the expression `x - y`, where *y* is an instance of a class providing an `__rsub__()` method, `type(y).__rsub__(y, x)` gets called if `type(x).__sub__(x, y)` returns [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) or `type(y)` is a subclass of `type(x)`. [5]

Be aware that `__rpow__()` should be defined to take an optional third argument when support for the three-argument form of the built-in [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) function is desired.

Changed in version 3.14: Three-argument [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) now attempts to call `__rpow__()` when needed. Formerly it was invoked solely in two-argument `pow()` and the binary power operator.

Note

Should the right operand have a type that subclasses the left operand's type, and should that subclass provide a distinct implementation of the operation's reflected method, this method runs ahead of the left operand's non-reflected method. Such behavior lets subclasses override the operations of their ancestors.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-numeric-types.md) · [Previous source section](object-add-self-and-other.md) · [Following source section](object-iadd-self-and-other.md)
