# ast: `ast.Call`

*class *ast.Call(*func*, *args*, *keywords*)

Represents a function call. The callable is `func`, which is frequently a `Name` or `Attribute` object. Regarding the arguments:

- The list of positionally passed arguments lives in `args`.

- The list of `keyword` objects standing for keyword-passed arguments lives in `keywords`.

Both `args` and `keywords` may be omitted, in which case they default to empty lists.

```pycon
>>> print(ast.dump(ast.parse('func(a, b=c, *d, **e)', mode='eval'), indent=4))
Expression(
    body=Call(
        func=Name(id='func', ctx=Load()),
        args=[
            Name(id='a', ctx=Load()),
            Starred(
                value=Name(id='d', ctx=Load()),
                ctx=Load())],
        keywords=[
            keyword(
                arg='b',
                value=Name(id='c', ctx=Load())),
            keyword(
                value=Name(id='e', ctx=Load()))]))

```

[Subject index](INDEX.md) · [Previous](ast-eq-class-to-ast-notin-class.md) · [Continue](ast-keyword-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
