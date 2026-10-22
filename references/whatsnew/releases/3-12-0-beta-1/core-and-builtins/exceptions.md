# Python 3.12.0 beta 1 / core and builtins / exceptions

[gh-103590](https://github.com/python/cpython/issues/103590): When a single exception emerges from a `try-except*` construct, leave it unwrapped rather than placing it inside an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup).

[gh-103492](https://github.com/python/cpython/issues/103492): Make the [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) for a literal `is` comparison clearer by naming which literal is at fault, given that `is` comparisons against e.g. `None` and bool literals are idiomatic.

[gh-77757](https://github.com/python/cpython/issues/77757): Exceptions thrown inside a typeobject's `__set_name__` method are no longer enclosed in a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). Instead, context is attached to the exception via a [**PEP 678**](https://peps.python.org/pep-0678/) note.

[gh-103333](https://github.com/python/cpython/issues/103333): [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) now keeps the `name` attribute across pickling and unpickling.

[gh-103899](https://github.com/python/cpython/issues/103899): Offer a useful hint inside the [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) message when a [module](https://docs.python.org/3.14/glossary.html#term-module) object is mistakenly called even though it owns a callable attribute sharing its name (for instance [`dis.dis()`](https://docs.python.org/3.14/library/dis.html#dis.dis) or [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
