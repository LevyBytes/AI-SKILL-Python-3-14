# object.__round__(*self*[, *ndigits*]) / object.__trunc__(*self*) / object.__floor__(*self*) / object.__ceil__(*self*)

object.__round__(*self*[, *ndigits*])

 object.__trunc__(*self*)

 object.__floor__(*self*)

 object.__ceil__(*self*)

Invoked to back the built-in function [`round()`](https://docs.python.org/3.14/library/functions.html#round) and the [`math`](https://docs.python.org/3.14/library/math.html#module-math) functions [`trunc()`](https://docs.python.org/3.14/library/math.html#math.trunc), [`floor()`](https://docs.python.org/3.14/library/math.html#math.floor) and [`ceil()`](https://docs.python.org/3.14/library/math.html#math.ceil). Except when *ndigits* is passed to `__round__()`, all these methods should return the object's value truncated to an [`Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral) (usually an [`int`](https://docs.python.org/3.14/library/functions.html#int)).

Changed in version 3.14: [`int()`](https://docs.python.org/3.14/library/functions.html#int) no longer delegates to the `__trunc__()` method.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-numeric-types.md) · [Previous source section](object-index.md) · [Following source section](with-statement-context-managers.md)
