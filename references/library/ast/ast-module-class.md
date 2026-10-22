# ast: `ast.Module`

### Root nodes

 *class *ast.Module(*body*, *type_ignores*)

A Python module, matching [file input](https://docs.python.org/3.14/reference/toplevel_components.html#file-input). It is the node type that `ast.parse()` produces under its default `"exec"` *mode*.

`body` is a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) of the module's Statements.

`type_ignores` is a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) holding the type ignore comments belonging to the module; consult `ast.parse()` for further specifics.

```pycon
>>> print(ast.dump(ast.parse('x = 1'), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=1))])

```

[Subject index](INDEX.md) · [Previous](node-classes.md) · [Continue](ast-expression-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
