# ast: Assignment type-comment fields

type_comment

The `type_comment` field is an optional string carrying the type annotation written as a comment.

```pycon
>>> print(ast.dump(ast.parse('a = b = 1'), indent=4)) # Multiple assignment
Module(
    body=[
        Assign(
            targets=[
                Name(id='a', ctx=Store()),
                Name(id='b', ctx=Store())],
            value=Constant(value=1))])

>>> print(ast.dump(ast.parse('a,b = c'), indent=4)) # Unpacking
Module(
    body=[
        Assign(
            targets=[
                Tuple(
                    elts=[
                        Name(id='a', ctx=Store()),
                        Name(id='b', ctx=Store())],
                    ctx=Store())],
            value=Name(id='c', ctx=Load()))])

```

[Subject index](INDEX.md) · [Previous](ast-assign-class.md) · [Continue](ast-annassign-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: ast.Assign](ast-assign-class.md) · [Owning module, declaration or section: Statements](ast-assign-class.md)
