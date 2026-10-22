# Python 3.9.0 beta 1 / library / ast

[bpo-40662](https://bugs.python.org/issue?@action=redirect&bpo=40662): Repaired [`ast.get_source_segment()`](https://docs.python.org/3.14/library/ast.html#ast.get_source_segment) when ast nodes carry incomplete location information. Irit Katriel wrote the patch.

[bpo-40355](https://bugs.python.org/issue?@action=redirect&bpo=40355): Sharpen the error reporting of [`ast.literal_eval()`](https://docs.python.org/3.14/library/ast.html#ast.literal_eval) when it meets malformed [`ast.Dict`](https://docs.python.org/3.14/library/ast.html#ast.Dict) nodes, rather than quietly skipping any non-conforming elements. Curtis Bucher wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
