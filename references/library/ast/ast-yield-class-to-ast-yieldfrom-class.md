# ast: `ast.Yield`, `ast.YieldFrom`

*class *ast.Yield(*value*)

 *class *ast.YieldFrom(*value*)

A `yield` or `yield from` expression. Since these count as expressions, they have to sit inside an `Expr` node whenever the value handed back goes unused.

```pycon
>>> print(ast.dump(ast.parse('yield x'), indent=4))
Module(
    body=[
        Expr(
            value=Yield(
                value=Name(id='x', ctx=Load())))])

>>> print(ast.dump(ast.parse('yield from x'), indent=4))
Module(
    body=[
        Expr(
            value=YieldFrom(
                value=Name(id='x', ctx=Load())))])

```

[Subject index](INDEX.md) · [Previous](ast-return-class.md) · [Continue](ast-global-class-to-ast-nonlocal-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Function and class definitions](ast-functiondef-class.md)
