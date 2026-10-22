# What's New In Python 3.6 / Other Language Changes

### Other Language Changes

A handful of more modest revisions landed in the core Python language:

- Any `global` or `nonlocal` statement is now required to appear in the text ahead of the first reference to the named variable inside that same scope. This used to produce a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning).

- You may now assign a [special method](https://docs.python.org/3.14/reference/datamodel.html#specialnames) the value `None` as a signal that the matching operation is unsupported. As an illustration, when a class assigns [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) to `None`, that class becomes non-iterable. (Contributed by Andrew Barnert and Ivan Levkivskyi in [bpo-25958](https://bugs.python.org/issue?@action=redirect&bpo=25958).)

- Extended runs of duplicated traceback lines now get condensed into `"[Previous line repeated {count} more times]"` (consult traceback for a demonstration). (Contributed by Emanuel Barry in [bpo-26823](https://bugs.python.org/issue?@action=redirect&bpo=26823).)

- The import machinery now throws the freshly added [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) (subclass of [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError)) whenever a module cannot be located. Existing code that catches ImportError (in try-except) keeps functioning. (Contributed by Eric Snow in [bpo-15767](https://bugs.python.org/issue?@action=redirect&bpo=15767).)

- Class methods that depend on a zero-argument `super()` now behave properly even when invoked from metaclass methods while a class is being created. (Contributed by Martin Teichmann in [bpo-23722](https://bugs.python.org/issue?@action=redirect&bpo=23722).)

[Subject index](INDEX.md) · [Previous source section](dtrace-and-systemtap-probing-support.md) · [Next source section](secrets.md) · [Release/subject declaration](summary-release-highlights.md)
