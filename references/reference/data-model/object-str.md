# object.__str__(*self*)

object.__str__(*self*)

Invoked by [`str(object)`](https://docs.python.org/3.14/library/stdtypes.html#str), by the default `__format__()` implementation, and by the built-in function [`print()`](https://docs.python.org/3.14/library/functions.html#print), to derive the “informal” or nicely printable string form of an object. A [str](https://docs.python.org/3.14/library/stdtypes.html#textseq) object must be the return value.

What sets this method apart from `object.__repr__()` is that `__str__()` carries no obligation to yield a valid Python expression: a handier or terser representation is acceptable.

The built-in type [`object`](https://docs.python.org/3.14/library/functions.html#object) defines a default implementation that invokes `object.__repr__()`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Following source section](object-repr.md) · [Previous source section](object-repr.md) · [Following source section](object-bytes.md)
