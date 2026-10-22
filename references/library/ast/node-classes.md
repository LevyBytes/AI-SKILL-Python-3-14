# ast: AST child-field and source-location attributes

_fields

On every concrete class sits a `_fields` attribute that lists the names of all of its child nodes.

For each child node, an instance of a concrete class carries one attribute, typed exactly as the grammar specifies. To take an example, the `left` attribute on `ast.BinOp` instances has type `ast.expr`.

Where the grammar tags such attributes as optional (with a question mark), the value can be `None`. Where attributes admit zero-or-more values (flagged with an asterisk), Python lists are used to hold them. When you compile an AST through [`compile()`](https://docs.python.org/3.14/library/functions.html#compile), every attribute that can appear must be present and carry a valid value.

 _field_types

Sitting on each concrete class, the `_field_types` attribute is a dictionary that pairs field names (the same ones in `_fields`) with their types.

```pycon
>>> ast.TypeVar._field_types
{'name': <class 'str'>, 'bound': ast.expr | None, 'default_value': ast.expr | None}

```

Added in version 3.13.

 lineno

 col_offset

 end_lineno

 end_col_offset

Subclass instances of `ast.expr` and `ast.stmt` carry `lineno`, `col_offset`, `end_lineno`, and `end_col_offset` attributes. Here `lineno` together with `end_lineno` give the opening and closing line numbers of the source text span (counted from 1, so the very first line is line 1), while `col_offset` and `end_col_offset` are the matching UTF-8 byte offsets of the first and final tokens that produced the node. That UTF-8 offset gets stored because UTF-8 is what the parser works in internally.

Keep in mind that the compiler does not need the end positions, so they are optional. An end offset points to the spot *after* the closing symbol; for instance, you can pull the source segment of a single-line expression node with `source_line[node.col_offset : node.end_col_offset]`.

A class `ast.T` constructor reads the arguments handed to it this way:

- When positional arguments are present, the count has to equal the number of entries in `T._fields`; each one becomes an attribute under those names.

- When keyword arguments are present, they populate the like-named attributes with whatever values you pass.

So, to build and fill in an `ast.UnaryOp` node, this would work:

```python
node = ast.UnaryOp(ast.USub(), ast.Constant(5, lineno=0, col_offset=0),
                   lineno=0, col_offset=0)

```

Leaving out a constructor field that the grammar marks optional gives it a default of `None`. Omit a list field and the default is the empty list. Omit a field whose type is `ast.expr_context` and `Load()` is the default. Omit any other field and you get a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning), with the AST node simply lacking that field. As of Python 3.15, that situation will instead raise an error.

Changed in version 3.8: Every constant now flows through the `ast.Constant` class.

Changed in version 3.9: A simple index shows up as its own value, while an extended slice shows up as a tuple.

Changed in version 3.13: Omitted fields gained reasonable defaults in the AST node constructors — an optional field now falls back to `None`, a list field falls back to an empty list, and an `ast.expr_context` field falls back to `Load()`. Before this, a left-out attribute simply was not present on the built node, and reading it triggered an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Changed in version 3.14: For `AST` nodes, the [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) result now shows the values held in the node fields.

Deprecated since version 3.8, removed in version 3.14: Earlier Python releases shipped the AST classes `ast.Num`, `ast.Str`, `ast.Bytes`, `ast.NameConstant` and `ast.Ellipsis`; all of them became deprecated back in Python 3.8. Python 3.14 dropped these classes, with `ast.Constant` now taking over what they did.

Deprecated since version 3.9: You can still reach the legacy `ast.Index` and `ast.ExtSlice` classes, though a coming Python release will drop them. For now, constructing either one yields an instance belonging to some other class.

Deprecated since version 3.13, will be removed in version 3.15: Earlier Python releases let you build AST nodes while leaving required fields out. In the same way, the AST node constructors accepted any keyword argument and stored it as an attribute on the AST node, even when no field of that node matched. Such behavior is deprecated, and Python 3.15 will drop it.

Note

The write-ups of the individual node classes shown here were first drawn from the wonderful [Green Tree Snakes](https://greentreesnakes.readthedocs.io/en/latest/) project along with everyone who contributed to it.

[Subject index](INDEX.md) · [Previous](ast-ast-class.md) · [Continue](ast-module-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: ast.AST](ast-ast-class.md) · [Owning module, declaration or section: Node classes](ast-ast-class.md)
