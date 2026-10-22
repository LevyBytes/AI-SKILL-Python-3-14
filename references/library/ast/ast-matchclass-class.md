# ast: `ast.MatchClass`

*class *ast.MatchClass(*cls*, *patterns*, *kwd_attrs*, *kwd_patterns*)

A class match pattern. An expression naming the nominal class to be matched is what `cls` is. A sequence of pattern nodes to compare against the class's declared sequence of pattern-matching attributes is what `patterns` is. A sequence of extra attributes to be matched (given as keyword arguments inside the class pattern) is what `kwd_attrs` is, while `kwd_patterns` are the matching patterns (given as keyword values inside the class pattern).

A match here happens when the subject is an instance of the named class, every positional pattern matches the respective class-declared attribute, and each given keyword attribute matches its respective pattern.

Note: a class may define a property returning self so that a pattern node can be matched against the very instance being matched. A handful of builtin types match that way too, in the manner laid out in the match statement documentation.

```pycon
>>> print(ast.dump(ast.parse("""
... match x:
...     case Point2D(0, 0):
...         ...
...     case Point3D(x=0, y=0, z=0):
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchClass(
                        cls=Name(id='Point2D', ctx=Load()),
                        patterns=[
                            MatchValue(
                                value=Constant(value=0)),
                            MatchValue(
                                value=Constant(value=0))]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchClass(
                        cls=Name(id='Point3D', ctx=Load()),
                        kwd_attrs=[
                            'x',
                            'y',
                            'z'],
                        kwd_patterns=[
                            MatchValue(
                                value=Constant(value=0)),
                            MatchValue(
                                value=Constant(value=0)),
                            MatchValue(
                                value=Constant(value=0))]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ast-matchmapping-class.md) · [Continue](ast-matchas-class.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: Pattern matching](ast-match-class.md)
