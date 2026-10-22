# Python 3.14.0 alpha 2 / core and builtins / code

[gh-126072](https://github.com/python/cpython/issues/126072): As a follow-on to [gh-126101](https://github.com/python/cpython/issues/126101), the [Code Objects](https://docs.python.org/3.14/c-api/code.html#codeobjects) produced for lambda, annotation and type alias no longer prepend `None` to their [`co_consts`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_consts).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
