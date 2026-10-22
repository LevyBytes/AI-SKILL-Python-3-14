# Python 3.11.0 beta 1 / core and builtins / exceptions

[gh-91479](https://github.com/python/cpython/issues/91479): Swap the `__note__` field of [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) (which an earlier 3.11 version had added) for the finished design from [**PEP 678**](https://peps.python.org/pep-0678/). Specifically, `BaseException` gains an `add_note()` method, while its `__notes__` field gets created on demand.

[bpo-43857](https://bugs.python.org/issue?@action=redirect&bpo=43857): Make the [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) text clearer when an absent attribute is deleted. Géry Ogam authored the patch.

[gh-81548](https://github.com/python/cpython/issues/81548): Octal escapes whose value exceeds `0o377` will now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). A later Python release turns these into a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) and, eventually, a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
