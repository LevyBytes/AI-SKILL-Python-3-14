# ast: `ast.MatchMapping`

*class *ast.MatchMapping(*keys*, *patterns*, *rest*)

A mapping match pattern. A sequence of expression nodes is what `keys` is. A matching sequence of pattern nodes is what `patterns` is. An optional name that may be given to grab the leftover mapping elements is what `rest` is. Allowed key expressions are limited in the manner laid out in the match statement documentation.

A match here happens when the subject is a mapping, every evaluated key expression is found in that mapping, and the value sitting under each key matches its respective subpattern. When `rest` is something other than `None`, a dict holding the leftover mapping elements gets bound to that name, provided the whole mapping pattern works out.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case {1: _, 2: _}:
...         ...
...     case {**rest}:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchMapping(
                        keys=[
                            Constant(value=1),
                            Constant(value=2)],
                        patterns=[
                            MatchAs(),
                            MatchAs()]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchMapping(rest='rest'),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ast-matchstar-class.md) · [Continue](ast-matchclass-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
