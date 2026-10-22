# Python 3.14.0 beta 2 / core and builtins / imports and modules

[gh-127960](https://github.com/python/cpython/issues/127960): The PyREPL interactive shell no longer launches with the `__package__` and `__file__` global names pointing at `_pyrepl` package internals. Contributed by Yuichiro Tachibana.

[gh-69605](https://github.com/python/cpython/issues/69605): While auto-completing an import inside the [REPL](https://docs.python.org/3.14/glossary.html#term-REPL), turning up no candidates now offers no suggestion at all, instead of pulling suggestions out of the current namespace.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
