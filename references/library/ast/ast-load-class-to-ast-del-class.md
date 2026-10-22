# ast: `ast.Load`, `ast.Store`, `ast.Del`

*class *ast.Load

 *class *ast.Store

 *class *ast.Del

A variable reference can serve to read a variable's value, to bind a fresh value to it, or to remove it. To tell these situations apart, each variable reference carries a context.

```pycon
>>> print(ast.dump(ast.parse('a'), indent=4))
Module(
    body=[
        Expr(
            value=Name(id='a', ctx=Load()))])

>>> print(ast.dump(ast.parse('a = 1'), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Name(id='a', ctx=Store())],
            value=Constant(value=1))])

>>> print(ast.dump(ast.parse('del a'), indent=4))
Module(
    body=[
        Delete(
            targets=[
                Name(id='a', ctx=Del())])])

```

[Subject index](INDEX.md) · [Previous](ast-name-class.md) · [Continue](ast-starred-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Variables](ast-name-class.md)
