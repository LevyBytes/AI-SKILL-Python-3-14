# ast: `ast.Global`, `ast.Nonlocal`

*class *ast.Global(*names*)

 *class *ast.Nonlocal(*names*)

`global` and `nonlocal` statements. A list of raw strings is what `names` is.

```pycon
>>> print(ast.dump(ast.parse('global x,y,z'), indent=4))
Module(
    body=[
        Global(
            names=[
                'x',
                'y',
                'z'])])

>>> print(ast.dump(ast.parse('nonlocal x,y,z'), indent=4))
Module(
    body=[
        Nonlocal(
            names=[
                'x',
                'y',
                'z'])])

```

[Subject index](INDEX.md) · [Previous](ast-yield-class-to-ast-yieldfrom-class.md) · [Continue](ast-classdef-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Function and class definitions](ast-functiondef-class.md)
