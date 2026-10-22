# ast: `ast.Try`

*class *ast.Try(*body*, *handlers*, *orelse*, *finalbody*)

Represents `try` blocks. Every attribute is a list of nodes to run, with the exception of `handlers`, which is a list of `ExceptHandler` nodes.

```pycon
>>> print(ast.dump(ast.parse("""
... try:
...    ...
... except Exception:
...    ...
... except OtherException as e:
...    ...
... else:
...    ...
... finally:
...    ...
... """), indent=4))
Module(
    body=[
        Try(
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            handlers=[
                ExceptHandler(
                    type=Name(id='Exception', ctx=Load()),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                ExceptHandler(
                    type=Name(id='OtherException', ctx=Load()),
                    name='e',
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])],
            orelse=[
                Expr(
                    value=Constant(value=Ellipsis))],
            finalbody=[
                Expr(
                    value=Constant(value=Ellipsis))])])

```

[Subject index](INDEX.md) · [Previous](ast-break-class-to-ast-continue-class.md) · [Continue](ast-trystar-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)
