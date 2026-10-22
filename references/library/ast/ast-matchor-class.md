# ast: `ast.MatchOr`

*class *ast.MatchOr(*patterns*)

A match "or-pattern". An or-pattern tries each of its subpatterns one after another against the subject until one of them works out. At that point the or-pattern is taken to have succeeded. Should no subpattern work out, the or-pattern fails. A list of match pattern nodes that get compared against the subject is held in the `patterns` attribute.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case [x] | (y):
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchOr(
                        patterns=[
                            MatchSequence(
                                patterns=[
                                    MatchAs(name='x')]),
                            MatchAs(name='y')]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ast-matchas-class.md) · [Continue](ast-typeignore-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
