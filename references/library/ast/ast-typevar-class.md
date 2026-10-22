# ast: `ast.TypeVar`

### Type parameters

[Type parameters](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) may appear on classes, functions, and type aliases.

 *class *ast.TypeVar(*name*, *bound*, *default_value*)

A [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar). The name of the type variable is what `name` is. The bound or the constraints, if there are any, is what `bound` is. When `bound` is a `Tuple`, it stands for constraints; otherwise it stands for the bound. The default value is what `default_value` is; should the `TypeVar` carry no default, this attribute gets set to `None`.

```pycon
>>> print(ast.dump(ast.parse("type Alias[T: int = bool] = list[T]"), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            type_params=[
                TypeVar(
                    name='T',
                    bound=Name(id='int', ctx=Load()),
                    default_value=Name(id='bool', ctx=Load()))],
            value=Subscript(
                value=Name(id='list', ctx=Load()),
                slice=Name(id='T', ctx=Load()),
                ctx=Load()))])

```

Added in version 3.12.

Changed in version 3.13: Added the *default_value* parameter.

[Subject index](INDEX.md) · [Previous](ast-typeignore-class.md) · [Continue](ast-paramspec-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
