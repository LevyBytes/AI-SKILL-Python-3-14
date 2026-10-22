# ast: `ast.While`

*class *ast.While(*test*, *body*, *orelse*)

Represents a `while` loop. The `test` field carries the condition, for instance a `Compare` node.

```pycon
>>> print(ast.dump(ast.parse("""
... while x:
...    ...
... else:
...    ...
... """), indent=4))
Module(
    body=[
        While(
            test=Name(id='x', ctx=Load()),
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            orelse=[
                Expr(
                    value=Constant(value=Ellipsis))])])

```

[Subject index](INDEX.md) · [Previous](ast-for-class.md) · [Continue](ast-break-class-to-ast-continue-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)
