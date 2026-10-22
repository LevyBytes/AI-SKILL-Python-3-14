# ast: `ast.Starred`

*class *ast.Starred(*value*, *ctx*)

A `*var` variable reference. The variable lives in `value`, usually as a `Name` node. You must use this type whenever you assemble a `Call` node that takes `*args`.

```pycon
>>> print(ast.dump(ast.parse('a, *b = it'), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Tuple(
                    elts=[
                        Name(id='a', ctx=Store()),
                        Starred(
                            value=Name(id='b', ctx=Store()),
                            ctx=Store())],
                    ctx=Store())],
            value=Name(id='it', ctx=Load()))])

```

[Subject index](INDEX.md) · [Previous](ast-load-class-to-ast-del-class.md) · [Continue](ast-expr-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Variables](ast-name-class.md)
