# ast: `ast.alias`

*class *ast.alias(*name*, *asname*)

Each of the two parameters is a raw string of the names. The `asname` field may be `None` when the plain name should be used.

```pycon
>>> print(ast.dump(ast.parse('from ..foo.bar import a as b, c'), indent=4))
Module(
    body=[
        ImportFrom(
            module='foo.bar',
            names=[
                alias(name='a', asname='b'),
                alias(name='c')],
            level=2)])

```

[Subject index](INDEX.md) · [Previous](ast-importfrom-class.md) · [Continue](ast-if-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Imports](ast-import-class.md)
