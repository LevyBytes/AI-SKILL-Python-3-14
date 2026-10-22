# ast: `ast.TypeVarTuple`

*class *ast.TypeVarTuple(*name*, *default_value*)

A [`typing.TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple). The name of the type variable tuple is what `name` is. The default value is what `default_value` is; should the `TypeVarTuple` carry no default, this attribute gets set to `None`.

```pycon
>>> print(ast.dump(ast.parse("type Alias[*Ts = ()] = tuple[*Ts]"), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            type_params=[
                TypeVarTuple(
                    name='Ts',
                    default_value=Tuple(ctx=Load()))],
            value=Subscript(
                value=Name(id='tuple', ctx=Load()),
                slice=Tuple(
                    elts=[
                        Starred(
                            value=Name(id='Ts', ctx=Load()),
                            ctx=Load())],
                    ctx=Load()),
                ctx=Load()))])

```

Added in version 3.12.

Changed in version 3.13: Added the *default_value* parameter.

[Subject index](INDEX.md) · [Previous](ast-paramspec-class.md) · [Continue](ast-functiondef-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Type parameters](ast-typevar-class.md)
