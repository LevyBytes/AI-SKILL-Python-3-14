# ast: `ast.NamedExpr`

*class *ast.NamedExpr(*target*, *value*)

Represents a named expression. The assignment expressions operator (popularly called the walrus operator) generates this AST node. Unlike the `Assign` node, whose first argument may consist of several nodes, here each of `target` and `value` is required to be a single node.

```pycon
>>> print(ast.dump(ast.parse('(x := 4)', mode='eval'), indent=4))
Expression(
    body=NamedExpr(
        target=Name(id='x', ctx=Store()),
        value=Constant(value=4)))

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](ast-attribute-class.md) · [Continue](ast-subscript-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
