# ast: `ast.Set`

*class *ast.Set(*elts*)

A set. Inside `elts` is a list of nodes that stand for the set's elements.

```pycon
>>> print(ast.dump(ast.parse('{1, 2, 3}', mode='eval'), indent=4))
Expression(
    body=Set(
        elts=[
            Constant(value=1),
            Constant(value=2),
            Constant(value=3)]))

```

[Subject index](INDEX.md) · [Previous](ast-list-class-to-ast-tuple-class.md) · [Continue](ast-dict-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Literals](ast-constant-class.md)
