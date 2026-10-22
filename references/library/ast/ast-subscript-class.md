# ast: `ast.Subscript`

#### Subscripting

 *class *ast.Subscript(*value*, *slice*, *ctx*)

Represents a subscript, for instance `l[1]`. The subscripted object, normally a sequence or mapping, is `value`. The `slice` may be an index, a slice, or a key; it is permitted to be a `Tuple` that holds a `Slice`. The `ctx` field is `Load`, `Store` or `Del` based on whatever action the subscript carries out.

```pycon
>>> print(ast.dump(ast.parse('l[1:2, 3]', mode='eval'), indent=4))
Expression(
    body=Subscript(
        value=Name(id='l', ctx=Load()),
        slice=Tuple(
            elts=[
                Slice(
                    lower=Constant(value=1),
                    upper=Constant(value=2)),
                Constant(value=3)],
            ctx=Load()),
        ctx=Load()))

```

[Subject index](INDEX.md) · [Previous](ast-namedexpr-class.md) · [Continue](ast-slice-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
