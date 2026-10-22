# ast: `ast.ImportFrom`

*class *ast.ImportFrom(*module*, *names*, *level*)

Stands for `from x import y`. The `module` field is a raw string of the ‘from’ name with no leading dots, or `None` for statements like `from . import foo`. The `level` field is an integer giving the relative import's level (where 0 denotes an absolute import).

```pycon
>>> print(ast.dump(ast.parse('from y import x,y,z'), indent=4))
Module(
    body=[
        ImportFrom(
            module='y',
            names=[
                alias(name='x'),
                alias(name='y'),
                alias(name='z')],
            level=0)])

```

[Subject index](INDEX.md) · [Previous](ast-import-class.md) · [Continue](ast-alias-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Imports](ast-import-class.md)
