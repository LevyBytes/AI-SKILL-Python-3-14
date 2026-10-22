# Python 3.14.0 alpha 1 / library / ast

[gh-91818](https://github.com/python/cpython/issues/91818): For the CLI across a range of modules ([`ast`](https://docs.python.org/3.14/library/ast.html#module-ast), [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip), [`json`](https://docs.python.org/3.14/library/json.html#module-json), [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb), [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3), [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize), [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv)), the usage message now shows the real executable name rather than just "python".

[gh-117865](https://github.com/python/cpython/issues/117865): Speed up importing the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module by holding off the [`re`](https://docs.python.org/3.14/library/re.html#module-re) import until needed. Jelle Zijlstra wrote the patch.

[bpo-15987](https://bugs.python.org/issue?@action=redirect&bpo=15987): [`ast.compare()`](https://docs.python.org/3.14/library/ast.html#ast.compare), which compares two ASTs, is now implemented. Batuhan Taskaya wrote the patch with assistance from Jeremy Hylton.

[gh-121332](https://github.com/python/cpython/issues/121332): Repair the constructor of [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) nodes that carry custom `_attributes`. Formerly, supplying custom attributes triggered a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Handing the constructor arguments absent from `_fields` or `_attributes` stays deprecated. Patch by Jelle Zijlstra.

[gh-121210](https://github.com/python/cpython/issues/121210): Deal with AST nodes whose runtime fields or attributes are absent inside [`ast.compare()`](https://docs.python.org/3.14/library/ast.html#ast.compare). Patch by Bénédikt Tran.

[gh-118851](https://github.com/python/cpython/issues/118851): For the constructors of [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) node classes, a missing `ctx` argument now falls back to [`ast.Load()`](https://docs.python.org/3.14/library/ast.html#ast.Load) by default. Jelle Zijlstra authored this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
