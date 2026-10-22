# ast: `ast.Expression`

*class *ast.Expression(*body*)

A lone Python [expression input](https://docs.python.org/3.14/reference/toplevel_components.html#expression-input). The node type `ast.parse()` returns whenever *mode* equals `"eval"`.

`body` is a single node, one of the expression types.

```pycon
>>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
Expression(
    body=Constant(value=123))

```

[Subject index](INDEX.md) · [Previous](ast-module-class.md) · [Continue](ast-interactive-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Root nodes](ast-module-class.md)
