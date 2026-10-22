# What's New In Python 3.13 / builtins

### builtins

- Drop support for chained [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) descriptors (which arrived through [gh-63272](https://github.com/python/cpython/issues/63272)). Wrapping other descriptors with them, such as [`property`](https://docs.python.org/3.14/library/functions.html#property), is no longer possible. This feature's underlying design was flawed and produced a number of problems. For a `classmethod` "pass-through", look at the `__wrapped__` attribute that arrived in Python 3.10. (Contributed by Raymond Hettinger in [gh-89519](https://github.com/python/cpython/issues/89519).)

- Trigger a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) whenever [`frame.clear()`](https://docs.python.org/3.14/reference/datamodel.html#frame.clear) is invoked on a suspended frame (mirroring the long-standing behaviour for an executing frame). (Contributed by Irit Katriel in [gh-79932](https://github.com/python/cpython/issues/79932).)

[Subject index](INDEX.md) · [Previous source section](2to3.md) · [Next source section](configparser.md) · [Release/subject declaration](summary-release-highlights.md)
