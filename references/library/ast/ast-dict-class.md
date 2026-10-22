# ast: `ast.Dict`

*class *ast.Dict(*keys*, *values*)

A dictionary. The `keys` and `values` lists carry the nodes that stand for the keys and the values, paired up in the same order (just what calling `dictionary.keys()` and `dictionary.values()` would hand back).

For dictionary unpacking written with dictionary literals, the expression you want expanded lands in the `values` list, and `keys` gets a `None` at the matching slot.

```pycon
>>> print(ast.dump(ast.parse('{"a":1, **d}', mode='eval'), indent=4))
Expression(
    body=Dict(
        keys=[
            Constant(value='a'),
            None],
        values=[
            Constant(value=1),
            Name(id='d', ctx=Load())]))

```

[Subject index](INDEX.md) · [Previous](ast-set-class.md) · [Continue](ast-name-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Literals](ast-constant-class.md)
