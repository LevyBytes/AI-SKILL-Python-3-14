# ast: `ast.JoinedStr`

*class *ast.JoinedStr(*values*)

An f-string, made up of a sequence of `FormattedValue` and `Constant` nodes.

```pycon
>>> print(ast.dump(ast.parse('f"sin({a}) is {sin(a):.3}"', mode='eval'), indent=4))
Expression(
    body=JoinedStr(
        values=[
            Constant(value='sin('),
            FormattedValue(
                value=Name(id='a', ctx=Load()),
                conversion=-1),
            Constant(value=') is '),
            FormattedValue(
                value=Call(
                    func=Name(id='sin', ctx=Load()),
                    args=[
                        Name(id='a', ctx=Load())]),
                conversion=-1,
                format_spec=JoinedStr(
                    values=[
                        Constant(value='.3')]))]))

```

[Subject index](INDEX.md) · [Previous](ast-formattedvalue-class.md) · [Continue](ast-templatestr-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Literals](ast-constant-class.md)
