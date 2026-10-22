# ast: `ast.For`

*class *ast.For(*target*, *iter*, *body*, *orelse*, *type_comment*)

Represents a `for` loop. The `target` field holds the variable(s) being assigned by the loop, as one `Name`, `Tuple`, `List`, `Attribute` or `Subscript` node. The `iter` field holds the item iterated over, once more as a single node. Both `body` and `orelse` contain lists of nodes to run. The ones in `orelse` run when the loop ends normally instead of through a `break` statement.

 type_comment

The `type_comment` field is an optional string carrying the type annotation written as a comment.

```pycon
>>> print(ast.dump(ast.parse("""
... for x in y:
...     ...
... else:
...     ...
... """), indent=4))
Module(
    body=[
        For(
            target=Name(id='x', ctx=Store()),
            iter=Name(id='y', ctx=Load()),
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            orelse=[
                Expr(
                    value=Constant(value=Ellipsis))])])

```

[Subject index](INDEX.md) · [Previous](ast-if-class.md) · [Continue](ast-while-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)
