# ast: `ast.Constant`

### Literals

 *class *ast.Constant(*value*, *kind*)

A constant value. On the `Constant` literal, the `value` attribute carries the Python object that it stands for. What it can represent are instances of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`complex`](https://docs.python.org/3.14/library/functions.html#complex), and [`bool`](https://docs.python.org/3.14/library/functions.html#bool), plus the constants [`None`](https://docs.python.org/3.14/library/constants.html#None) and [`Ellipsis`](https://docs.python.org/3.14/library/constants.html#Ellipsis).

The `kind` attribute is an optional string. With string literals carrying a `u` prefix, `kind` becomes `'u'`. Everywhere else, `kind` is `None`.

```pycon
>>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
Expression(
    body=Constant(value=123))
>>> print(ast.dump(ast.parse("u'hello'", mode='eval'), indent=4))
Expression(
    body=Constant(value='hello', kind='u'))

```

[Subject index](INDEX.md) · [Previous](ast-functiontype-class.md) · [Continue](ast-formattedvalue-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
