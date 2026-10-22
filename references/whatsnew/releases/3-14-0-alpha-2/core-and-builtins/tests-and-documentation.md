# Python 3.14.0 alpha 2 / core and builtins / tests and documentation

[gh-126072](https://github.com/python/cpython/issues/126072): A fresh flag has been introduced in [`co_flags`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_flags) that signals whether the leading entry of [`co_consts`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_consts) holds the docstring. When a code object lacks a docstring, `None` will **NOT** be inserted.

[gh-125444](https://github.com/python/cpython/issues/125444): Resolve an illegal instruction on older Arm architectures. Patch by Diego Russo, testing by Ross Burton.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
