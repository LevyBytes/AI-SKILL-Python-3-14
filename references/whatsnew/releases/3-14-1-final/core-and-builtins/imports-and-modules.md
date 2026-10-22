# Python 3.14.1 final / core and builtins / imports and modules

[gh-133400](https://github.com/python/cpython/issues/133400): Restored Ctrl+D (^D) behavior inside the _pyrepl module so it lines up with the former pre-3.13 REPL behavior.

[gh-141930](https://github.com/python/cpython/issues/141930): During a module import, rely on Python’s standard file object to guarantee that writes targeting `.pyc` files either finish or surface a suitable error.

[gh-69605](https://github.com/python/cpython/issues/69605): Resolve the case of certain standard library submodules being absent from the [REPL](https://docs.python.org/3.14/glossary.html#term-REPL) auto-completion of imports.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
