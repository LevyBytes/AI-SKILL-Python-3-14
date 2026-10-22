# ast: `ast.TypeAlias`

*class *ast.TypeAlias(*name*, *type_params*, *value*)

Represents a [type alias](https://docs.python.org/3.14/library/typing.html#type-aliases) defined via the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement. The `name` field is the alias's name, `type_params` is a list of type parameters, and `value` is the type alias's value.

```pycon
>>> print(ast.dump(ast.parse('type Alias = int'), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            value=Name(id='int', ctx=Load()))])

```

Added in version 3.12.

Further statements that apply solely within functions or loops are covered in separate sections.

[Subject index](INDEX.md) · [Previous](ast-pass-class.md) · [Continue](ast-import-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Statements](ast-assign-class.md)
