# ast: `ast.FormattedValue`

*class *ast.FormattedValue(*value*, *conversion*, *format_spec*)

A node that stands for one formatting field inside an f-string. Should the string hold just a single formatting field and nothing more, the node can stand alone; otherwise it sits inside `JoinedStr`.

- Any expression node can be `value` — for instance a literal, a variable, or a call to a function.

- `conversion` is an integer:

  - -1: no formatting

  - 97 (`ord('a')`): `!a` [`ASCII`](https://docs.python.org/3.14/library/functions.html#ascii) formatting

  - 114 (`ord('r')`): `!r` [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) formatting

  - 115 (`ord('s')`): `!s` [`string`](https://docs.python.org/3.14/library/stdtypes.html#str) formatting

- `format_spec` is a `JoinedStr` node that captures how the value is formatted, or it is `None` when no format was given. You may assign `conversion` and `format_spec` together.

[Subject index](INDEX.md) · [Previous](ast-constant-class.md) · [Continue](ast-joinedstr-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Literals](ast-constant-class.md)
