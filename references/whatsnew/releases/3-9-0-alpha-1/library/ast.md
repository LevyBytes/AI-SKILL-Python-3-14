# Python 3.9.0 alpha 1 / library / ast

[bpo-18374](https://bugs.python.org/issue?@action=redirect&bpo=18374): Repaired the `.col_offset` attribute on nested [`ast.BinOp`](https://docs.python.org/3.14/library/ast.html#ast.BinOp) instances, which under certain conditions carried a value that was far too large.

[bpo-38049](https://bugs.python.org/issue?@action=redirect&bpo=38049): A command-line interface was added for the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module.

[bpo-37995](https://bugs.python.org/issue?@action=redirect&bpo=37995): The *indent* option was added to [`ast.dump()`](https://docs.python.org/3.14/library/ast.html#ast.dump), enabling it to emit multiline indented output.

[bpo-37950](https://bugs.python.org/issue?@action=redirect&bpo=37950): Fixed [`ast.dump()`](https://docs.python.org/3.14/library/ast.html#ast.dump) when invoked on an incompletely initialized node.

[bpo-36917](https://bugs.python.org/issue?@action=redirect&bpo=36917): Provided a default implementation of the [`ast.NodeVisitor.visit_Constant()`](https://docs.python.org/3.14/library/ast.html#ast.NodeVisitor.visit_Constant) method, which raises a deprecation warning and routes to the matching `visit_Num()`, `visit_Str()`, and similar methods.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
