# sys.ps1, sys.ps2

sys.ps1

sys.ps2

Strings that specify the primary and secondary prompt of the interpreter. They exist only when the interpreter is in interactive mode, where their starting values are `'>>> '` and `'... '`. Should a non-string object get assigned to one of these variables, the interpreter re-evaluates its [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) every time it prepares to read a fresh interactive command; you can exploit this to construct a dynamic prompt.

[API family](INDEX.md) · [sys context index](../INDEX.md).
