# Python 3.12.0 alpha 2 / core and builtins / exceptions

[gh-99139](https://github.com/python/cpython/issues/99139): Sharpen the hint offered for [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exceptions on instances. When a method triggers a `NameError` and the instance carries an attribute matching exactly the name in that exception, the recommendation now points at `self.<NAME>` rather than the nearest candidate found within the method's scope. Pablo Galindo wrote the patch

[gh-98401](https://github.com/python/cpython/issues/98401): Octal escapes whose value exceeds `0o377` (for instance `"\477"`), which were deprecated back in Python 3.11, now emit a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) rather than a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). A later Python release will ultimately turn these into a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). Victor Stinner authored the patch.

[gh-98401](https://github.com/python/cpython/issues/98401): A backslash followed by a character that does not form a valid escape sequence now raises a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) instead of a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). To illustrate, `re.compile("\d+\.\d+")` will now warn with `SyntaxWarning` (since `"\d"` is not a valid escape); prefer raw strings for regular expressions, such as `re.compile(r"\d+\.\d+")`. Down the road, a future Python release will switch from `SyntaxWarning` to raising [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). Victor Stinner authored the patch.

[gh-98931](https://github.com/python/cpython/issues/98931): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) wording shown when somebody writes `import x from y` rather than `from y import x`. Pablo Galindo wrote the patch

[gh-99257](https://github.com/python/cpython/issues/99257): Resolve a problem where member descriptors (for example, the ones backing [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__)) might misbehave or crash rather than raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when reached through an instance whose type is invalid.

[gh-93143](https://github.com/python/cpython/issues/93143): Instead of mutating `co_code`, the interpreter now emits a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) and binds [`None`](https://docs.python.org/3.14/library/constants.html#None) to whatever fast locals remain unbound following jumps or [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) statements that run while tracing is active.

[gh-91058](https://github.com/python/cpython/issues/91058): An [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) thrown by a failing `from <module> import <name>` now ships suggestions for `<name>`, drawn from the names that `<module>` makes available. Pablo Galindo wrote the patch

[gh-99153](https://github.com/python/cpython/issues/99153): Correct where the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) is located for a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) block carrying both [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) and [`except*`](https://docs.python.org/3.14/reference/compound_stmts.html#except-star).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
