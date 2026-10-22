# Python 3.8.0 alpha 1 / library / compiler and parser

[bpo-35733](https://bugs.python.org/issue?@action=redirect&bpo=35733): `ast.Constant(boolean)` is no longer an instance of `ast.Num`. Patch by Anthony Sottile.

[bpo-34515](https://bugs.python.org/issue?@action=redirect&bpo=34515): Corrected parsing of non-ASCII identifiers within `lib2to3.pgen2.tokenize` ([**PEP 3131**](https://peps.python.org/pep-3131/)).

[bpo-33308](https://bugs.python.org/issue?@action=redirect&bpo=33308): Repaired a crash in the `parser` module while turning an ST object into a tree of tuples or lists with `line_info=False` and `col_info=True`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
