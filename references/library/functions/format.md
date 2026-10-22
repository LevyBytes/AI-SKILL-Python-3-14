# Built-in Functions

format(*value*, *format_spec=''*, */*)

Turn a *value* into a “formatted” representation, governed by *format_spec*. How *format_spec* is read hinges on the type of the *value* argument; even so, there exists a standard formatting syntax that most built-in types follow: [Format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec).

By default *format_spec* is an empty string, which generally produces the same result as calling [`str(value)`](https://docs.python.org/3.14/library/stdtypes.html#str).

Invoking `format(value, format_spec)` gets converted into `type(value).__format__(value, format_spec)`, which skips over the instance dictionary while looking for the value's [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) method. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception arises when the method search arrives at `object` while the *format_spec* is non-empty, or when either the *format_spec* or the return value is not a string.

Changed in version 3.4: `object().__format__(format_spec)` raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) if *format_spec* is not an empty string.

[Subject index](INDEX.md) · [Previous](float-class-to-float-class.md) · [Continue](frozenset-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
