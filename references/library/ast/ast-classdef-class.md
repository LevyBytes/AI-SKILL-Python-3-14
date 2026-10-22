# ast: `ast.ClassDef`

*class *ast.ClassDef(*name*, *bases*, *keywords*, *body*, *decorator_list*, *type_params*)

A class definition.

- `name` is a raw string for the class name

- `bases` is a list of nodes for explicitly specified base classes.

- `keywords` lists `keyword` nodes, chiefly for "metaclass". Any other keywords get handed on to the metaclass, following [**PEP 3115**](https://peps.python.org/pep-3115/).

- `body` lists the nodes that stand for the code held within the class definition.

- `decorator_list` is a list of nodes, as in `FunctionDef`.

- `type_params` is a list of type parameters.

```pycon
>>> print(ast.dump(ast.parse("""\
... @decorator1
... @decorator2
... class Foo(base1, base2, metaclass=meta):
...     pass
... """), indent=4))
Module(
    body=[
        ClassDef(
            name='Foo',
            bases=[
                Name(id='base1', ctx=Load()),
                Name(id='base2', ctx=Load())],
            keywords=[
                keyword(
                    arg='metaclass',
                    value=Name(id='meta', ctx=Load()))],
            body=[
                Pass()],
            decorator_list=[
                Name(id='decorator1', ctx=Load()),
                Name(id='decorator2', ctx=Load())])])

```

Changed in version 3.12: Added `type_params`.

[Subject index](INDEX.md) · [Previous](ast-global-class-to-ast-nonlocal-class.md) · [Continue](ast-asyncfunctiondef-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Function and class definitions](ast-functiondef-class.md)
