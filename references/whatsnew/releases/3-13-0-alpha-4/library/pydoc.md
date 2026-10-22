# Python 3.13.0 alpha 4 / library / pydoc

[gh-97959](https://github.com/python/cpython/issues/97959): Correct the rendering of class methods, bound methods, plus method and function aliases inside [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc). Class methods no longer carry the "method of builtins.type instance" note. Matching notes now accompany class and unbound methods. Method and function aliases now point back to the module or class where the origin lived when that differs from the current one. Bound methods now appear under the static methods section. Methods on builtin classes are now handled along with methods on Python classes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
