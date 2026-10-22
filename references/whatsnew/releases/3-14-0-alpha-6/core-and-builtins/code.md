# Python 3.14.0 alpha 6 / core and builtins / code

[gh-130851](https://github.com/python/cpython/issues/130851): On the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build, a crash that arose while building a [`code`](https://docs.python.org/3.14/library/code.html#module-code) object whose [`co_consts`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_consts) held instances of types the bytecode compiler does not itself emit has been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
