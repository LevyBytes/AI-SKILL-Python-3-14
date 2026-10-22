# ast: `ast.Raise`

*class *ast.Raise(*exc*, *cause*)

Represents a `raise` statement. The `exc` field is the exception object being raised, usually a `Call` or `Name`, or `None` for a bare `raise`. The `cause` field is the optional portion supplying `y` in `raise x from y`.

```pycon
>>> print(ast.dump(ast.parse('raise x from y'), indent=4))
Module(
    body=[
        Raise(
            exc=Name(id='x', ctx=Load()),
            cause=Name(id='y', ctx=Load()))])

```

[Subject index](INDEX.md) · [Previous](ast-augassign-class.md) · [Continue](ast-assert-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Statements](ast-assign-class.md)
