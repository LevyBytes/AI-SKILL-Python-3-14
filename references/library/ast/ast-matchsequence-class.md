# ast: `ast.MatchSequence`

*class *ast.MatchSequence(*patterns*)

A sequence match pattern. The patterns that get compared against the subject's elements when the subject is a sequence are what `patterns` holds. A sequence of variable length is matched when any one of the subpatterns is a `MatchStar` node; otherwise a fixed length sequence is matched.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case [1, 2]:
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
                                value=Constant(value=2))]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ast-matchsingleton-class.md) · [Continue](ast-matchstar-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
