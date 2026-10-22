# ast: `ast.AnnAssign`

*class *ast.AnnAssign(*target*, *annotation*, *value*, *simple*)

Represents an assignment carrying a type annotation. The `target` field is one node and may be a `Name`, an `Attribute` or a `Subscript`. The `annotation` field is the annotation itself, for example a `Constant` or `Name` node. The `value` field is a single optional node.

The `simple` field is always 0 (marking a “complex” target) or 1 (marking a “simple” target). A target counts as “simple” only when it is just a `Name` node not enclosed in parentheses; everything else is regarded as complex. The [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) dictionary of modules and classes lists simple targets exclusively.

```pycon
>>> print(ast.dump(ast.parse('c: int'), indent=4))
Module(
    body=[
        AnnAssign(
            target=Name(id='c', ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            simple=1)])

>>> print(ast.dump(ast.parse('(a): int = 1'), indent=4)) # Annotation with parenthesis
Module(
    body=[
        AnnAssign(
            target=Name(id='a', ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            value=Constant(value=1),
            simple=0)])

>>> print(ast.dump(ast.parse('a.b: int'), indent=4)) # Attribute annotation
Module(
    body=[
        AnnAssign(
            target=Attribute(
                value=Name(id='a', ctx=Load()),
                attr='b',
                ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            simple=0)])

>>> print(ast.dump(ast.parse('a[1]: int'), indent=4)) # Subscript annotation
Module(
    body=[
        AnnAssign(
            target=Subscript(
                value=Name(id='a', ctx=Load()),
                slice=Constant(value=1),
                ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            simple=0)])

```

[Subject index](INDEX.md) · [Previous](statements.md) · [Continue](ast-augassign-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Statements](ast-assign-class.md)
