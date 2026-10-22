# Built-in Functions

setattr(*object*, *name*, *value*, */*)

Think of this as the mirror image of `getattr()`. It takes an object, a string, and a value of any kind. That string can refer to an attribute that already exists or to a brand-new one. The function writes the value into the attribute, as long as the object permits it. So `setattr(x, 'foobar', 123)` amounts to the same thing as `x.foobar = 123`.

The *name* doesn't have to be a Python identifier in the sense laid out in [Names (identifiers and keywords)](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers), unless the object decides to require that — say, within a custom [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) or through [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__). When an attribute's name isn't a valid identifier, dot notation can't reach it, though `getattr()` and similar functions still can.

Note

Given that [private name mangling](https://docs.python.org/3.14/reference/expressions.html#private-name-mangling) takes place when code is compiled, you have to mangle a private attribute's name yourself (attributes carrying two leading underscores) before you can assign it via `setattr()`.

[Subject index](INDEX.md) · [Previous](set-class.md) · [Continue](slice-class-to-slice-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
