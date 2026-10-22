# ast: `ast.withitem`

*class *ast.withitem(*context_expr*, *optional_vars*)

Represents one context manager inside a `with` block. The `context_expr` field is the context manager, frequently a `Call` node. The `optional_vars` field is a `Name`, `Tuple` or `List` for the `as foo` portion, or `None` when it is absent.

```pycon
>>> print(ast.dump(ast.parse("""\
... with a as b, c as d:
...    something(b, d)
... """), indent=4))
Module(
    body=[
        With(
            items=[
                withitem(
                    context_expr=Name(id='a', ctx=Load()),
                    optional_vars=Name(id='b', ctx=Store())),
                withitem(
                    context_expr=Name(id='c', ctx=Load()),
                    optional_vars=Name(id='d', ctx=Store()))],
            body=[
                Expr(
                    value=Call(
                        func=Name(id='something', ctx=Load()),
                        args=[
                            Name(id='b', ctx=Load()),
                            Name(id='d', ctx=Load())]))])])

```

[Subject index](INDEX.md) · [Previous](ast-with-class.md) · [Continue](ast-match-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)
