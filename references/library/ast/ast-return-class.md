# ast: `ast.Return`

*class *ast.Return(*value*)

A `return` statement.

```pycon
>>> print(ast.dump(ast.parse('return 4'), indent=4))
Module(
    body=[
        Return(
            value=Constant(value=4))])

```

[Subject index](INDEX.md) · [Previous](ast-arg-class.md) · [Continue](ast-yield-class-to-ast-yieldfrom-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Function and class definitions](ast-functiondef-class.md)
