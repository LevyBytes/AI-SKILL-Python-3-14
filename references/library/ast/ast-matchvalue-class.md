# ast: `ast.MatchValue`

*class *ast.MatchValue(*value*)

A literal or value match pattern whose comparison is by equality. An expression node is what `value` holds. The value nodes that are allowed are limited in the manner laid out in the match statement documentation. A match here happens when the match subject equals the value once evaluated.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case "Relevant":
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchValue(
                        value=Constant(value='Relevant')),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](pattern-matching.md) · [Continue](ast-matchsingleton-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
