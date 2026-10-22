# Python 3.12.0 alpha 4 / core and builtins / exceptions

[gh-87447](https://github.com/python/cpython/issues/87447): Resolve a spurious [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) during comprehension rebind checking for names that are not in fact redefined.

Rebinding `b` in `[(b := 1) for a, b.prop in some_iter]` is now permitted. Per [**PEP 572**](https://peps.python.org/pep-0572/), rebinding `a` stays forbidden.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
