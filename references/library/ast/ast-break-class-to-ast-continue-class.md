# ast: `ast.Break`, `ast.Continue`

*class *ast.Break

 *class *ast.Continue

These are the `break` and `continue` statements.

```pycon
>>> print(ast.dump(ast.parse("""\
... for a in b:
...     if a > 5:
...         break
...     else:
...         continue
...
... """), indent=4))
Module(
    body=[
        For(
            target=Name(id='a', ctx=Store()),
            iter=Name(id='b', ctx=Load()),
            body=[
                If(
                    test=Compare(
                        left=Name(id='a', ctx=Load()),
                        ops=[
                            Gt()],
                        comparators=[
                            Constant(value=5)]),
                    body=[
                        Break()],
                    orelse=[
                        Continue()])])])

```

[Subject index](INDEX.md) · [Previous](ast-while-class.md) · [Continue](ast-try-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Control flow](ast-if-class.md)
