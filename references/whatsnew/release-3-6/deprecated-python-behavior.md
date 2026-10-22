# What's New In Python 3.6 / Deprecated Python behavior

### Deprecated Python behavior

Raising the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception within a generator now yields a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning), and is set to provoke a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) come Python 3.7. Refer to [PEP 479: Change StopIteration handling inside generators](https://docs.python.org/3.14/whatsnew/3.5.html#whatsnew-pep-479) for the specifics.

The [`__aiter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aiter__) method is now supposed to hand back an asynchronous iterator straightaway in place of returning an awaitable like it used to. Choosing the older route raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Backward compatibility disappears in Python 3.7. (Contributed by Yury Selivanov in [bpo-27243](https://bugs.python.org/issue?@action=redirect&bpo=27243).)

A backslash-character pair that fails to form a valid escape sequence now produces a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Even though this is destined to turn into a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) someday, that change is several Python releases away. (Contributed by Emanuel Barry in [bpo-27364](https://bugs.python.org/issue?@action=redirect&bpo=27364).)

While carrying out a relative import, leaning on `__name__` and `__path__` from the calling module when `__spec__` or `__package__` go undefined now raises an [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning). (Contributed by Rose Ames in [bpo-25791](https://bugs.python.org/issue?@action=redirect&bpo=25791).)

[Subject index](INDEX.md) · [Previous source section](new-keywords.md) · [Next source section](deprecated-python-modules-functions-and-methods-asynchat.md) · [Release/subject declaration](summary-release-highlights.md)
