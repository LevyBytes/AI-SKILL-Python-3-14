# ast: `ast.BinOp`

*class *ast.BinOp(*left*, *op*, *right*)

Represents a binary operation, for instance addition or division. The operator is `op`, while `left` and `right` may each be any expression node.

```pycon
>>> print(ast.dump(ast.parse('x + y', mode='eval'), indent=4))
Expression(
    body=BinOp(
        left=Name(id='x', ctx=Load()),
        op=Add(),
        right=Name(id='y', ctx=Load())))

```

[Subject index](INDEX.md) · [Previous](ast-uadd-class-to-ast-invert-class.md) · [Continue](ast-add-class-to-ast-matmult-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
