# ast: `ast.List`, `ast.Tuple`

*class *ast.List(*elts*, *ctx*)

 *class *ast.Tuple(*elts*, *ctx*)

A list or tuple. Inside `elts` is a list of nodes that stand for the elements. `ctx` becomes `Store` when the container serves as an assignment target (that is, `(x,y)=something`), and is `Load` in every other case.

```pycon
>>> print(ast.dump(ast.parse('[1, 2, 3]', mode='eval'), indent=4))
Expression(
    body=List(
        elts=[
            Constant(value=1),
            Constant(value=2),
            Constant(value=3)],
        ctx=Load()))
>>> print(ast.dump(ast.parse('(1, 2, 3)', mode='eval'), indent=4))
Expression(
    body=Tuple(
        elts=[
            Constant(value=1),
            Constant(value=2),
            Constant(value=3)],
        ctx=Load()))

```

[Subject index](INDEX.md) · [Previous](ast-interpolation-class.md) · [Continue](ast-set-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Literals](ast-constant-class.md)
