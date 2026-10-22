# ast: `ast.AugAssign`

*class *ast.AugAssign(*target*, *op*, *value*)

Represents augmented assignment, for example `a += 1`. Below, `target` is a `Name` node for `x` (carrying the `Store` context), `op` is `Add`, and `value` is a `Constant` whose value is 1.

The `target` attribute may not be a `Tuple` or `List`, which differs from the targets allowed in `Assign`.

```pycon
>>> print(ast.dump(ast.parse('x += 2'), indent=4))
Module(
    body=[
        AugAssign(
            target=Name(id='x', ctx=Store()),
            op=Add(),
            value=Constant(value=2))])

```

[Subject index](INDEX.md) · [Previous](ast-annassign-class.md) · [Continue](ast-raise-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Statements](ast-assign-class.md)
