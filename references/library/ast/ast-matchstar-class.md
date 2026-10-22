# ast: `ast.MatchStar`

*class *ast.MatchStar(*name*)

Captures whatever remains of the sequence inside a variable length sequence match pattern. When `name` is something other than `None`, a list holding the leftover sequence elements gets bound to that name, provided the whole sequence pattern works out.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case [1, 2, *rest]:
...         ...
...     case [*_]:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchSequence(
                        patterns=[
                            MatchValue(
                                value=Constant(value=1)),
                            MatchValue(
                                value=Constant(value=2)),
                            MatchStar(name='rest')]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchSequence(
                        patterns=[
                            MatchStar()]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ast-matchsequence-class.md) · [Continue](ast-matchmapping-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
