# ast: `ast.ExceptHandler`

*class *ast.ExceptHandler(*type*, *name*, *body*)

Represents a single `except` clause. The `type` field is the exception type to be matched, typically a `Name` node (or `None` for a catch-all `except:` clause). The `name` field is a raw string for the name bound to the exception, or `None` when the clause lacks `as foo`. The `body` field is a list of nodes.

```pycon
>>> print(ast.dump(ast.parse("""\
... try:
...     a + 1
... except TypeError:
...     pass
... """), indent=4))
Module(
    body=[
        Try(
            body=[
                Expr(
                    value=BinOp(
                        left=Name(id='a', ctx=Load()),
                        op=Add(),
                        right=Constant(value=1)))],
            handlers=[
                ExceptHandler(
                    type=Name(id='TypeError', ctx=Load()),
                    body=[
                        Pass()])])])

```

[Subject index](INDEX.md) · [Previous](ast-trystar-class.md) · [Continue](ast-with-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)
