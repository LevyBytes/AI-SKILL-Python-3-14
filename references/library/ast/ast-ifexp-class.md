# ast: `ast.IfExp`

*class *ast.IfExp(*test*, *body*, *orelse*)

Represents an expression of the form `a if b else c`. A single node fills each field, so for the case below every one of the three is a `Name` node.

```pycon
>>> print(ast.dump(ast.parse('a if b else c', mode='eval'), indent=4))
Expression(
    body=IfExp(
        test=Name(id='b', ctx=Load()),
        body=Name(id='a', ctx=Load()),
        orelse=Name(id='c', ctx=Load())))

```

[Subject index](INDEX.md) · [Previous](ast-keyword-class.md) · [Continue](ast-attribute-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
