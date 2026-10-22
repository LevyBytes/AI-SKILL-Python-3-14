# ast: `ast.Slice`

*class *ast.Slice(*lower*, *upper*, *step*)

Represents ordinary slicing (written either `lower:upper` or `lower:upper:step`). It is valid only within the *slice* field of `Subscript`, whether placed there directly or as one element inside a `Tuple`.

```pycon
>>> print(ast.dump(ast.parse('l[1:2]', mode='eval'), indent=4))
Expression(
    body=Subscript(
        value=Name(id='l', ctx=Load()),
        slice=Slice(
            lower=Constant(value=1),
            upper=Constant(value=2)),
        ctx=Load()))

```

[Subject index](INDEX.md) · [Previous](ast-subscript-class.md) · [Continue](ast-listcomp-class-to-ast-dictcomp-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Subscripting](ast-subscript-class.md)
