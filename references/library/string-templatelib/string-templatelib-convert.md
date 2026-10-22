# string.templatelib — Helper functions

### Helper functions

 string.templatelib.convert(*obj*, */*, *conversion*)

Brings formatted string literal [conversion](https://docs.python.org/3.14/library/string.html#formatstrings-conversion) semantics to bear on the supplied object *obj*. This often comes in handy when you are writing your own template string processing logic.

At present there are three conversion flags on offer:

- `'s'`, which invokes [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) on the value (matching `!s`),

- `'r'`, which invokes [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) (matching `!r`), and

- `'a'`, which invokes [`ascii()`](https://docs.python.org/3.14/library/functions.html#ascii) (matching `!a`).

Where the conversion flag is `None`, *obj* comes back untouched.

[Subject index](INDEX.md) · [Previous](string-templatelib-interpolation-new.md) · [Continue](../stringprep/stringprep-in-table-a1-to-stringprep-in-table-c9.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md)
