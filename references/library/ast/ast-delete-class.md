# ast: `ast.Delete`

*class *ast.Delete(*targets*)

Stands for a `del` statement. The `targets` field is a list of nodes, for instance `Name`, `Attribute` or `Subscript` nodes.

```pycon
>>> print(ast.dump(ast.parse('del x,y,z'), indent=4))
Module(
    body=[
        Delete(
            targets=[
                Name(id='x', ctx=Del()),
                Name(id='y', ctx=Del()),
                Name(id='z', ctx=Del())])])

```

[Subject index](INDEX.md) · [Previous](ast-assert-class.md) · [Continue](ast-pass-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Statements](ast-assign-class.md)
