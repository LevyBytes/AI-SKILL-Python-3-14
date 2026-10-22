# ast: `ast.Compare`

*class *ast.Compare(*left*, *ops*, *comparators*)

Represents a comparison among two or more values. The starting value is `left`, the operator list is `ops`, and `comparators` is the list of every value that follows the first one in the comparison.

```pycon
>>> print(ast.dump(ast.parse('1 <= a < 10', mode='eval'), indent=4))
Expression(
    body=Compare(
        left=Constant(value=1),
        ops=[
            LtE(),
            Lt()],
        comparators=[
            Name(id='a', ctx=Load()),
            Constant(value=10)]))

```

[Subject index](INDEX.md) · [Previous](ast-and-class-to-ast-or-class.md) · [Continue](ast-eq-class-to-ast-notin-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Expressions](ast-expr-class.md)
