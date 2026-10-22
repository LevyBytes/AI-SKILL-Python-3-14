# object.__format__(*self*, *format_spec*)

object.__format__(*self*, *format_spec*)

Invoked by the [`format()`](https://docs.python.org/3.14/library/functions.html#format) built-in function and, by extension, during evaluation of [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method, to yield a “formatted” string form of an object. The *format_spec* argument is a string carrying a description of the wanted formatting options. How the *format_spec* argument is read rests with the type that implements `__format__()`; even so, most classes either hand off formatting to one of the built-in types or adopt a comparable formatting-option syntax.

Refer to [Format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec) for an account of the standard formatting syntax.

A string object must be the return value.

The [`object`](https://docs.python.org/3.14/library/functions.html#object) class’s default implementation expects an empty *format_spec* string. It hands off to `__str__()`.

Changed in version 3.4: The __format__ method belonging to `object` itself raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when handed any non-empty string.

Changed in version 3.7: `object.__format__(x, '')` now amounts to `str(x)` instead of `format(str(x), '')`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Previous source section](object-bytes.md) · [Following source section](object-lt-object-le-object-eq-object-ne-object-gt-object-ge.md)
