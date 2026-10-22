# ast: `ast.Expr`

### Expressions

 *class *ast.Expr(*value*)

Whenever an expression — a function call, say — stands on its own as a statement while its return value goes neither used nor stored, this container wraps it. `value` carries one of this section's other nodes: a `Constant`, a `Name`, a `Lambda`, a `Yield` or `YieldFrom` node.

```pycon
>>> print(ast.dump(ast.parse('-a'), indent=4))
Module(
    body=[
        Expr(
            value=UnaryOp(
                op=USub(),
                operand=Name(id='a', ctx=Load())))])

```

[Subject index](INDEX.md) · [Previous](ast-starred-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
