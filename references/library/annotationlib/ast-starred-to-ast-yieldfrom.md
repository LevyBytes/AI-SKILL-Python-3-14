# annotationlib - Limitations of the `STRING` format - Contract: `ast.Starred` (`*` unpacking)

[`ast.Starred`](https://docs.python.org/3.14/library/ast.html#ast.Starred) (`*` unpacking)

- [`ast.Name`](https://docs.python.org/3.14/library/ast.html#ast.Name)

- [`ast.List`](https://docs.python.org/3.14/library/ast.html#ast.List)

- [`ast.Tuple`](https://docs.python.org/3.14/library/ast.html#ast.Tuple)

- [`ast.Slice`](https://docs.python.org/3.14/library/ast.html#ast.Slice)

Those below are unsupported, yet the stringifier raises a helpful error upon meeting them:

- [`ast.FormattedValue`](https://docs.python.org/3.14/library/ast.html#ast.FormattedValue) (f-strings; the error slips by undetected once conversion specifiers such as `!r` come into play)

- [`ast.JoinedStr`](https://docs.python.org/3.14/library/ast.html#ast.JoinedStr) (f-strings)

Those below are unsupported and lead to wrong output:

- [`ast.BoolOp`](https://docs.python.org/3.14/library/ast.html#ast.BoolOp) (`and` and `or`)

- [`ast.IfExp`](https://docs.python.org/3.14/library/ast.html#ast.IfExp)

- [`ast.Lambda`](https://docs.python.org/3.14/library/ast.html#ast.Lambda)

- [`ast.ListComp`](https://docs.python.org/3.14/library/ast.html#ast.ListComp)

- [`ast.SetComp`](https://docs.python.org/3.14/library/ast.html#ast.SetComp)

- [`ast.DictComp`](https://docs.python.org/3.14/library/ast.html#ast.DictComp)

- [`ast.GeneratorExp`](https://docs.python.org/3.14/library/ast.html#ast.GeneratorExp)

Those below are forbidden inside annotation scopes and hence beside the point:

- [`ast.NamedExpr`](https://docs.python.org/3.14/library/ast.html#ast.NamedExpr) (`:=`)

- [`ast.Await`](https://docs.python.org/3.14/library/ast.html#ast.Await)

- [`ast.Yield`](https://docs.python.org/3.14/library/ast.html#ast.Yield)

- [`ast.YieldFrom`](https://docs.python.org/3.14/library/ast.html#ast.YieldFrom)

[Subject index](INDEX.md) · [Previous](ast-binop-to-ast-subscript.md) · [Continue](limitations-of-the-forwardref-format.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md) · [Owning module, declaration or section: Limitations of the `STRING` format](ast-binop-to-ast-subscript.md)
