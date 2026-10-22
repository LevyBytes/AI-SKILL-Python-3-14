# ast: `ast.ListComp`, `ast.SetComp`, `ast.GeneratorExp`, `ast.DictComp`

#### Comprehensions

 *class *ast.ListComp(*elt*, *generators*)

 *class *ast.SetComp(*elt*, *generators*)

 *class *ast.GeneratorExp(*elt*, *generators*)

 *class *ast.DictComp(*key*, *value*, *generators*)

These cover list and set comprehensions, generator expressions, plus dictionary comprehensions. The field `elt` (or the pair `key` and `value`) is one node standing for the portion that gets evaluated against every item.

The field `generators` holds a list of `comprehension` nodes.

```pycon
>>> print(ast.dump(
...     ast.parse('[x for x in numbers]', mode='eval'),
...     indent=4,
... ))
Expression(
    body=ListComp(
        elt=Name(id='x', ctx=Load()),
        generators=[
            comprehension(
                target=Name(id='x', ctx=Store()),
                iter=Name(id='numbers', ctx=Load()),
                is_async=0)]))
>>> print(ast.dump(
...     ast.parse('{x: x**2 for x in numbers}', mode='eval'),
...     indent=4,
... ))
Expression(
    body=DictComp(
        key=Name(id='x', ctx=Load()),
        value=BinOp(
            left=Name(id='x', ctx=Load()),
            op=Pow(),
            right=Constant(value=2)),
        generators=[
            comprehension(
                target=Name(id='x', ctx=Store()),
                iter=Name(id='numbers', ctx=Load()),
                is_async=0)]))
>>> print(ast.dump(
...     ast.parse('{x for x in numbers}', mode='eval'),
...     indent=4,
... ))
Expression(
    body=SetComp(
        elt=Name(id='x', ctx=Load()),
        generators=[
            comprehension(
                target=Name(id='x', ctx=Store()),
                iter=Name(id='numbers', ctx=Load()),
                is_async=0)]))

```

[Subject index](INDEX.md) · [Previous](ast-slice-class.md) · [Continue](ast-comprehension-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)
