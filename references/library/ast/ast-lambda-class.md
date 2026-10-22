# ast: `ast.Lambda`

*class *ast.Lambda(*args*, *body*)

`lambda` is a stripped-down function definition usable within an expression. In contrast to `FunctionDef`, `body` carries just one node.

```pycon
>>> print(ast.dump(ast.parse('lambda x,y: ...'), indent=4))
Module(
    body=[
        Expr(
            value=Lambda(
                args=arguments(
                    args=[
                        arg(arg='x'),
                        arg(arg='y')]),
                body=Constant(value=Ellipsis)))])

```

[Subject index](INDEX.md) · [Previous](function-and-class-definitions.md) · [Continue](ast-arguments-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Function and class definitions](ast-functiondef-class.md)
