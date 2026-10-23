# ast - Type annotations

### Type annotations

 *class *ast.TypeIgnore(*lineno*, *tag*)

A `# type: ignore` comment sitting at *lineno*. The optional tag given through the form `# type: ignore <tag>` is what *tag* is.

```pycon
>>> print(ast.dump(ast.parse('x = 1 # type: ignore', type_comments=True), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=1))],
    type_ignores=[
        TypeIgnore(lineno=1, tag='')])
>>> print(ast.dump(ast.parse('x: bool = 1 # type: ignore[assignment]', type_comments=True), indent=4))
Module(
    body=[
        AnnAssign(
            target=Name(id='x', ctx=Store()),
            annotation=Name(id='bool', ctx=Load()),
            value=Constant(value=1),
            simple=1)],
    type_ignores=[
        TypeIgnore(lineno=1, tag='[assignment]')])

```

Note

No `TypeIgnore` nodes get produced while the *type_comments* parameter stays at `False` (its default). Consult `ast.parse()` for further detail.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](ast-matchor-class.md) · [Continue](ast-typevar-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
