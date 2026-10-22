# ast: `ast.MatchSingleton`

*class *ast.MatchSingleton(*value*)

A literal match pattern that does its comparison by identity. The singleton to compare against is what `value` holds: `None`, `True`, or `False`. A match here happens when the match subject is that very constant.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case None:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchSingleton(value=None),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ast-matchvalue-class.md) · [Continue](ast-matchsequence-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
