# ast: `ast.Await`

*class *ast.Await(*value*)

An `await` expression. Whatever it is waiting on is what `value` is. Valid solely inside the body of an `AsyncFunctionDef`.

```pycon
>>> print(ast.dump(ast.parse("""\
... async def f():
...     await other_func()
... """), indent=4))
Module(
    body=[
        AsyncFunctionDef(
            name='f',
            args=arguments(),
            body=[
                Expr(
                    value=Await(
                        value=Call(
                            func=Name(id='other_func', ctx=Load()))))])])

```

[Subject index](INDEX.md) · [Previous](ast-asyncfunctiondef-class.md) · [Continue](ast-asyncfor-class-to-ast-asyncwith-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Async and await](ast-asyncfunctiondef-class.md)
