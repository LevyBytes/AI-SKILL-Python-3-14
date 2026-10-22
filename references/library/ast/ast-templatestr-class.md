# ast: `ast.TemplateStr`

*class *ast.TemplateStr(*values*, */*)

Added in version 3.14.

A node standing for a template string literal, made up of a sequence of `Interpolation` and `Constant` nodes. The nodes may sit in any order and need not be interleaved.

```pycon
>>> expr = ast.parse('t"{name} finished {place:ordinal}"', mode='eval')
>>> print(ast.dump(expr, indent=4))
Expression(
    body=TemplateStr(
        values=[
            Interpolation(
                value=Name(id='name', ctx=Load()),
                str='name',
                conversion=-1),
            Constant(value=' finished '),
            Interpolation(
                value=Name(id='place', ctx=Load()),
                str='place',
                conversion=-1,
                format_spec=JoinedStr(
                    values=[
                        Constant(value='ordinal')]))]))

```

[Subject index](INDEX.md) · [Previous](ast-joinedstr-class.md) · [Continue](ast-interpolation-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Literals](ast-constant-class.md)
