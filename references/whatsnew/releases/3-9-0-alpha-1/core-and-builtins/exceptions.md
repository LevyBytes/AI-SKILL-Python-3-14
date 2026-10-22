# Python 3.9.0 alpha 1 / core and builtins / exceptions

[bpo-38631](https://bugs.python.org/issue?@action=redirect&bpo=38631): Substitute a plain [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) exception for the `Py_FatalError()` call inside `float.__getformat__()`.

[bpo-32912](https://bugs.python.org/issue?@action=redirect&bpo=32912): Backed out [bpo-32912](https://bugs.python.org/issue?@action=redirect&bpo=32912): the change that emitted [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) rather than [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) for invalid escape sequences inside string and bytes literals.

[bpo-37757](https://bugs.python.org/issue?@action=redirect&bpo=37757): [**PEP 572**](https://peps.python.org/pep-0572/): Following the PEP's description, assignment expressions henceforth raise [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) once their interplay with comprehension scoping yields an ambiguous target scope.

That `TargetScopeError` subclass the PEP first proposed has been dropped, in favour of simply raising ordinary syntax errors for the prohibited cases.

[bpo-34880](https://bugs.python.org/issue?@action=redirect&bpo=34880): Zackery Spytz contributed a fix so the [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statement behaves correctly even while the [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) exception is shadowed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
