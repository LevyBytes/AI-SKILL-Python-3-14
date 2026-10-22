# ast: `ast.BoolOp`

*class *ast.BoolOp(*op*, *values*)

Represents a boolean operation, either ‘or’ or ‘and’. The `op` field is set to `Or` or `And`. The operands appear in `values`. When the same operator repeats in a row, as with `a or b or c`, the whole chain folds into a single node carrying multiple values.

Note that `not` is excluded here, since it maps instead to a `UnaryOp`.

```pycon
>>> print(ast.dump(ast.parse('x or y', mode='eval'), indent=4))
Expression(
    body=BoolOp(
        op=Or(),
        values=[
            Name(id='x', ctx=Load()),
            Name(id='y', ctx=Load())]))

```

[Subject index](INDEX.md) · [Previous](ast-add-class-to-ast-matmult-class.md) · [Continue](ast-and-class-to-ast-or-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
