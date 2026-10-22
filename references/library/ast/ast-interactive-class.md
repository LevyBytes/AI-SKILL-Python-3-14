# ast: `ast.Interactive`

*class *ast.Interactive(*body*)

A single [interactive input](https://docs.python.org/3.14/reference/toplevel_components.html#interactive), of the kind seen in [Interactive Mode](https://docs.python.org/3.14/tutorial/appendix.html#tut-interac). The node type `ast.parse()` returns whenever *mode* equals `"single"`.

`body` is a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) of statement nodes.

```pycon
>>> print(ast.dump(ast.parse('x = 1; y = 2', mode='single'), indent=4))
Interactive(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=1)),
        Assign(
            targets=[
                Name(id='y', ctx=Store())],
            value=Constant(value=2))])

```

[Subject index](INDEX.md) · [Previous](ast-expression-class.md) · [Continue](ast-functiontype-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Root nodes](ast-module-class.md)
