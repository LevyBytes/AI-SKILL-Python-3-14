# ast: `ast.Import`

#### Imports

 *class *ast.Import(*names*)

Represents an import statement. The `names` field is a list of `alias` nodes.

```pycon
>>> print(ast.dump(ast.parse('import x,y,z'), indent=4))
Module(
    body=[
        Import(
            names=[
                alias(name='x'),
                alias(name='y'),
                alias(name='z')])])

```

[Subject index](INDEX.md) · [Previous](ast-typealias-class.md) · [Continue](ast-importfrom-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
