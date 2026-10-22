# ast: `ast.MatchAs`

*class *ast.MatchAs(*pattern*, *name*)

A match "as-pattern", capture pattern or wildcard pattern. The match pattern that the subject gets compared against is held in `pattern`. Should the pattern be `None`, the node stands for a capture pattern (that is, a bare name) and never fails.

The name that gets bound when the pattern works out is held in the `name` attribute. Should `name` be `None`, then `pattern` has to be `None` too, and the node stands for the wildcard pattern.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case [x] as y:
...         ...
...     case _:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchAs(
                        pattern=MatchSequence(
                            patterns=[
                                MatchAs(name='x')]),
                        name='y'),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchAs(),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ast-matchclass-class.md) · [Continue](ast-matchor-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
