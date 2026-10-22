# Python 3.9.0 alpha 5 / library / ast

[bpo-39999](https://bugs.python.org/issue?@action=redirect&bpo=39999): For the AST node classes, `__module__` now reports "ast" rather than "_ast". Docstrings were also added for placeholder AST node classes along with deprecated attributes.

[bpo-36287](https://bugs.python.org/issue?@action=redirect&bpo=36287): Optional fields and attributes carrying their default values are no longer emitted by [`ast.dump()`](https://docs.python.org/3.14/library/ast.html#ast.dump). For AST nodes, the defaults of optional fields and attributes are now declared as class attributes (so, for example, `Constant.kind` becomes `None`).

[bpo-39889](https://bugs.python.org/issue?@action=redirect&bpo=39889): Corrected [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) where extended slices hold a lone element (for example `a[i:j,]`). Drop superfluous tuples when indexing using a tuple (for example `a[i, j]`).

[bpo-34822](https://bugs.python.org/issue?@action=redirect&bpo=34822): The AST for subscription was simplified. A plain value now stands in for simple indices, while tuples represent extended slices. The [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) classes `Index` and `ExtSlice` are regarded as deprecated and will disappear in upcoming Python versions. Until then, `Index(value)` hands back the `value` itself, and `ExtSlice(slices)` hands back `Tuple(slices, Load())`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
