# What’s New In Python 3.8 / ast - ast

> (Contributed by Barry Warsaw and Jason R. Coombs in [bpo-34632](https://bugs.python.org/issue?@action=redirect&bpo=34632).)

### Improved Modules

### ast

Every AST node now carries `end_lineno` and `end_col_offset` attributes, pinpointing exactly where that node finishes. (Only nodes already bearing `lineno` and `col_offset` attributes gain this.)

A newly added [`ast.get_source_segment()`](https://docs.python.org/3.14/library/ast.html#ast.get_source_segment) hands back the source text tied to one particular AST node.

> (Contributed by Ivan Levkivskyi in [bpo-33416](https://bugs.python.org/issue?@action=redirect&bpo=33416).)

Several fresh flags have landed on the [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) function:

- `type_comments=True` makes it surface the text of [**PEP 484**](https://peps.python.org/pep-0484/) plus [**PEP 526**](https://peps.python.org/pep-0526/) type comments tied to certain AST nodes;

- `mode='func_type'` serves to parse [**PEP 484**](https://peps.python.org/pep-0484/) "signature type comments" (handed back for function definition AST nodes);

- `feature_version=(3, N)` lets you name an older Python 3 release. As one case, `feature_version=(3, 4)` treats [`async`](https://docs.python.org/3.14/reference/compound_stmts.html#async) and [`await`](https://docs.python.org/3.14/reference/expressions.html#await) as words that stay unreserved.

[Subject index](INDEX.md) · [Previous source section](new-modules.md) · [Next source section](asyncio.md) · [Release/subject declaration](assignment-expressions.md)
