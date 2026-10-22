# Python 3.11.0 alpha 1 / idle / apply highlighting fresh match statement s soft keywords match

[bpo-44010](https://bugs.python.org/issue?@action=redirect&bpo=44010): Apply highlighting to the fresh [match](https://docs.python.org/3.14/reference/compound_stmts.html#match) statement's [soft keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords): [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match), `case`, and [`_`](https://docs.python.org/3.14/reference/compound_stmts.html#wildcard-patterns). That highlighting, however, is imperfect and will be wrong in a few uncommon situations, among them certain `_`-s within `case` patterns.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
