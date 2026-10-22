# ast: `ast.Interpolation`

*class *ast.Interpolation(*value*, *str*, *conversion*, *format_spec=None*)

Added in version 3.14.

A node standing for one interpolation field inside a template string literal.

- Any expression node can be `value` — a literal, a variable, or a function call, for example. It carries the identical meaning to `FormattedValue.value`.

- `str` is a constant containing the text of the interpolation expression.

When `str` holds `None`, `value` is what gets used to emit code as `ast.unparse()` runs. That no longer promises the emitted code will match the original byte-for-byte and exists to serve code generation.

- `conversion` is an integer:

  - -1: no conversion

  - 97 (`ord('a')`): `!a` [`ASCII`](https://docs.python.org/3.14/library/functions.html#ascii) conversion

  - 114 (`ord('r')`): `!r` [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) conversion

  - 115 (`ord('s')`): `!s` [`string`](https://docs.python.org/3.14/library/stdtypes.html#str) conversion

This has the same meaning as `FormattedValue.conversion`.

- `format_spec` is a `JoinedStr` node that captures how the value is formatted, or it is `None` when no format was given. You may assign `conversion` and `format_spec` together. It carries the identical meaning to `FormattedValue.format_spec`.

[Subject index](INDEX.md) · [Previous](ast-templatestr-class.md) · [Continue](ast-list-class-to-ast-tuple-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Literals](ast-constant-class.md)
