# Python 3.11.0 alpha 1 / core and builtins / exceptions

[bpo-44589](https://bugs.python.org/issue?@action=redirect&bpo=44589): A mapping pattern inside a `match` statement that repeats two or more identical literal keys will now trigger a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) at compile-time.

[bpo-44348](https://bugs.python.org/issue?@action=redirect&bpo=44348): The deallocator of the [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) type now leans on the trashcan mechanism to head off stack overflow. Consider a raised [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) instance: it may chain to a further RecursionError by way of the `__context__` attribute or the `__traceback__` attribute, forming a chain of exceptions. Tearing down that chain can let nested deallocator calls crash with stack overflow whenever the chain runs too long for the stack memory on hand. Victor Stinner contributed the patch.

[bpo-12022](https://bugs.python.org/issue?@action=redirect&bpo=12022): For objects that lack support for the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) or [asynchronous context manager](https://docs.python.org/3.14/glossary.html#term-asynchronous-context-manager) protocols, [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) and [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statements respectively now raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) in place of an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

[bpo-44838](https://bugs.python.org/issue?@action=redirect&bpo=44838): Corrected a bug where the parser would emit a wrong custom [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) for malformed "if" expressions. Pablo Galindo supplied the fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
