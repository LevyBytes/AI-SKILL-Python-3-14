# ast: `ast.Attribute`

*class *ast.Attribute(*value*, *attr*, *ctx*)

Represents attribute access, for example `d.keys`. The `value` field is a node, generally a `Name`. The `attr` field is a plain string holding the attribute's name, and `ctx` is `Load`, `Store` or `Del` depending on the operation applied to the attribute.

```pycon
>>> print(ast.dump(ast.parse('snake.colour', mode='eval'), indent=4))
Expression(
    body=Attribute(
        value=Name(id='snake', ctx=Load()),
        attr='colour',
        ctx=Load()))

```

[Subject index](INDEX.md) · [Previous](ast-ifexp-class.md) · [Continue](ast-namedexpr-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
