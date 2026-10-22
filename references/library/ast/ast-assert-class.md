# ast: `ast.Assert`

*class *ast.Assert(*test*, *msg*)

Represents an assertion. The `test` field carries the condition, for instance a `Compare` node. The `msg` field carries the failure message.

```pycon
>>> print(ast.dump(ast.parse('assert x,y'), indent=4))
Module(
    body=[
        Assert(
            test=Name(id='x', ctx=Load()),
            msg=Name(id='y', ctx=Load()))])

```

[Subject index](INDEX.md) · [Previous](ast-raise-class.md) · [Continue](ast-delete-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Statements](ast-assign-class.md)
