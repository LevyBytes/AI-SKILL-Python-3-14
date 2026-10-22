# Python 3.13.0 beta 1 / core and builtins / exceptions

[gh-118513](https://github.com/python/cpython/issues/118513): Correct a spurious [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) arising when two comprehensions in one function each mention the same name, with that name bound in one comprehension yet treated as an implicit global in the other.

[gh-118082](https://github.com/python/cpython/issues/118082): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) message for imports lacking names, as occurs with `from x import` and `import`. The text now reminds users that [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) requires at least one name to follow it.

[gh-118090](https://github.com/python/cpython/issues/118090): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) message produced by empty type param brackets.

[gh-117536](https://github.com/python/cpython/issues/117536): Clear up a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) raised by a call to `agen.aclose().throw(Exception)`.

[gh-95754](https://github.com/python/cpython/issues/95754): Make the error message clearer when a script that shadows a standard library module triggers [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). Likewise, sharpen the message when a script shadowing a third party module reaches for an attribute on that third party module while it is still initialising.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
