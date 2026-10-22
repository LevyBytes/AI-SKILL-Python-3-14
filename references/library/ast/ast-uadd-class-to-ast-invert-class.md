# ast: `ast.UAdd`, `ast.USub`, `ast.Not`, `ast.Invert`

*class *ast.UAdd

 *class *ast.USub

 *class *ast.Not

 *class *ast.Invert

These are the tokens for unary operators. The `not` keyword corresponds to `Not`, and the `~` operator corresponds to `Invert`.

```pycon
>>> print(ast.dump(ast.parse('not x', mode='eval'), indent=4))
Expression(
    body=UnaryOp(
        op=Not(),
        operand=Name(id='x', ctx=Load())))

```

[Subject index](INDEX.md) · [Previous](ast-unaryop-class.md) · [Continue](ast-binop-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
