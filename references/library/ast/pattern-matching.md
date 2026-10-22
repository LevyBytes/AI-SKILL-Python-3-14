# ast: Match-case pattern, guard and body fields

One case clause within a `match` statement. The match pattern that the subject gets compared against is held in `pattern`. Be aware that the `AST` nodes generated for patterns are not the same as those generated for expressions, even where the surface syntax happens to coincide.

An expression that gets evaluated whenever the pattern matches the subject is held in the `guard` attribute.

A list of nodes to run when the pattern matches and evaluating the guard expression yields true is held in `body`.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case [x] if x>0:
...         ...
...     case tuple():
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
                            MatchAs(name='x')]),
                    guard=Compare(
                        left=Name(id='x', ctx=Load()),
                        ops=[
                            Gt()],
                        comparators=[
                            Constant(value=0)]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchClass(
                        cls=Name(id='tuple', ctx=Load())),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Continue](ast-matchvalue-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: ast.match_case](ast-match-case-class.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md) · [Preceding source contract and version conditions](ast-match-case-class.md)
