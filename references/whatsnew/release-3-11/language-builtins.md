# What's New In Python 3.11 / Language/Builtins

### Language/Builtins

- Stacking [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) descriptors (which came in via [bpo-19072](https://bugs.python.org/issue?@action=redirect&bpo=19072)) is now deprecated. Wrapping other descriptors such as [`property`](https://docs.python.org/3.14/library/functions.html#property) with it is no longer allowed. This capability rested on a flawed core design that spawned a series of downstream troubles. When you want a `classmethod` to “pass-through”, reach for the `__wrapped__` attribute introduced in Python 3.10. (Contributed by Raymond Hettinger in [gh-89519](https://github.com/python/cpython/issues/89519).)

- Within string and bytes literals, octal escapes whose value tops `0o377` (255 in decimal) now trigger a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). A later Python release will turn that into a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning), and ultimately into a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). (Contributed by Serhiy Storchaka in [gh-81548](https://github.com/python/cpython/issues/81548).)

- Having [`int()`](https://docs.python.org/3.14/library/functions.html#int) fall back to [`__trunc__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__trunc__) is now deprecated. Where `type(a)` defines `__trunc__()` yet omits [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) and [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__), invoking `int(a)` now triggers a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). (Contributed by Zackery Spytz in [bpo-44977](https://bugs.python.org/issue?@action=redirect&bpo=44977).)

[Subject index](INDEX.md) · [Previous source section](deprecated.md) · [Next source section](modules.md) · [Release/subject declaration](summary-release-highlights.md)
