# ast: `ast.TryStar`

*class *ast.TryStar(*body*, *handlers*, *orelse*, *finalbody*)

Represents `try` blocks that carry `except*` clauses. Its attributes match those of `Try`, except that the `ExceptHandler` nodes inside `handlers` are read as `except*` blocks rather then `except`.

```pycon
>>> print(ast.dump(ast.parse("""
... try:
...    ...
... except* Exception:
...    ...
... """), indent=4))
Module(
    body=[
        TryStar(
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            handlers=[
                ExceptHandler(
                    type=Name(id='Exception', ctx=Load()),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](ast-try-class.md) · [Continue](ast-excepthandler-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)
