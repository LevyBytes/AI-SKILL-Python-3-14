# What's new in Python 3.14 / ast - ast, copy

### ast

- Add [`compare()`](https://docs.python.org/3.14/library/ast.html#ast.compare), which performs a comparison between a pair of ASTs. (Contributed by Batuhan Taskaya and Jeremy Hylton in [gh-60191](https://github.com/python/cpython/issues/60191).)

- Add support for [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) for AST nodes. (Contributed by Bénédikt Tran in [gh-121141](https://github.com/python/cpython/issues/121141).)

- At optimization level 2, docstrings are now stripped out of an optimized AST. (Contributed by Irit Katriel in [gh-123958](https://github.com/python/cpython/issues/123958).)

-

For AST nodes, the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) result now carries additional detail. (Contributed by Tomas Roun in [gh-116022](https://github.com/python/cpython/issues/116022).)

- Given an AST as its argument, the [`parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) function will from now on confirm that the root node carries a suitable type. (Contributed by Irit Katriel in [gh-130139](https://github.com/python/cpython/issues/130139).)

- Fresh options were added to the command-line interface: [`--feature-version`](https://docs.python.org/3.14/library/ast.html#cmdoption-ast-feature-version), [`--optimize`](https://docs.python.org/3.14/library/ast.html#cmdoption-ast-optimize), and [`--show-empty`](https://docs.python.org/3.14/library/ast.html#cmdoption-ast-show-empty). (Contributed by Semyon Moroz in [gh-133367](https://github.com/python/cpython/issues/133367).)

### ast

- Drop the classes listed below, which have stood as deprecated aliases of [`Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) since Python 3.8 and have raised deprecation warnings since Python 3.12:

  - `Bytes`

  - `Ellipsis`

  - `NameConstant`

  - `Num`

  - `Str`

Because of these removals, user-supplied `visit_Num`, `visit_Str`, `visit_Bytes`, `visit_NameConstant` and `visit_Ellipsis` methods on custom [`NodeVisitor`](https://docs.python.org/3.14/library/ast.html#ast.NodeVisitor) subclasses will no longer fire while the `NodeVisitor` subclass is walking an AST. Instead, supply a `visit_Constant` method.

(Contributed by Alex Waygood in [gh-119562](https://github.com/python/cpython/issues/119562).)

- Drop the deprecated properties listed below on [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant), which existed to stay compatible with the now-removed AST classes:

  - `Constant.n`

  - `Constant.s`

Reach for `Constant.value` in their place. (Contributed by Alex Waygood in [gh-119562](https://github.com/python/cpython/issues/119562).)

[Subject index](INDEX.md) · [Previous source section](argparse.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](asyncio-task-behavior-changes.md) · [Next source section](asyncio-main-and-main.md)
