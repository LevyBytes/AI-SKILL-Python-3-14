# ast: `ast.If`

### Control flow

Note

When optional clauses such as `else` are absent, they are kept as an empty list.

 *class *ast.If(*test*, *body*, *orelse*)

Represents an `if` statement. The `test` field carries a single node, for instance a `Compare` node. Each of `body` and `orelse` carries a list of nodes.

There is no dedicated AST representation for `elif` clauses; instead they show up as additional `If` nodes nested in the `orelse` portion of the preceding one.

```pycon
>>> print(ast.dump(ast.parse("""
... if x:
...    ...
... elif y:
...    ...
... else:
...    ...
... """), indent=4))
Module(
    body=[
        If(
            test=Name(id='x', ctx=Load()),
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            orelse=[
                If(
                    test=Name(id='y', ctx=Load()),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))],
                    orelse=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

[Subject index](INDEX.md) · [Previous](ast-alias-class.md) · [Continue](ast-for-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
