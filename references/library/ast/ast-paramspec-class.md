# ast: `ast.ParamSpec`

*class *ast.ParamSpec(*name*, *default_value*)

A [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec). The name of the parameter specification is what `name` is. The default value is what `default_value` is; should the `ParamSpec` carry no default, this attribute gets set to `None`.

```pycon
>>> print(ast.dump(ast.parse("type Alias[**P = [int, str]] = Callable[P, int]"), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            type_params=[
                ParamSpec(
                    name='P',
                    default_value=List(
                        elts=[
                            Name(id='int', ctx=Load()),
                            Name(id='str', ctx=Load())],
                        ctx=Load()))],
            value=Subscript(
                value=Name(id='Callable', ctx=Load()),
                slice=Tuple(
                    elts=[
                        Name(id='P', ctx=Load()),
                        Name(id='int', ctx=Load())],
                    ctx=Load()),
                ctx=Load()))])

```

Added in version 3.12.

Changed in version 3.13: Added the *default_value* parameter.

[Subject index](INDEX.md) · [Previous](ast-typevar-class.md) · [Continue](ast-typevartuple-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Type parameters](ast-typevar-class.md)
