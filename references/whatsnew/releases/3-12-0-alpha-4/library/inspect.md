# Python 3.12.0 alpha 4 / library / inspect

[gh-83035](https://github.com/python/cpython/issues/83035): Repair how [`inspect.getsource()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsource) deals with decorator calls that use nested parentheses.

[gh-94912](https://github.com/python/cpython/issues/94912): Add the [`inspect.markcoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.markcoroutinefunction) decorator, which lets you flag a function as a coroutine by hand so that `iscoroutinefunction()` recognizes it.

[gh-85267](https://github.com/python/cpython/issues/85267): Several refinements to how [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) deals with `__text_signature`. - Repairs a situation in which `inspect.signature()` silently lost parameters - Repairs a situation in which `inspect.signature()` threw [`tokenize.TokenError`](https://docs.python.org/3.14/library/tokenize.html#tokenize.TokenError) - Teaches `inspect.signature()` to handle defaults built from binary operations over constant operands - Although its docs promise that `inspect.signature()` raises only [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), it occasionally threw [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError); such situations now produce `ValueError` instead - Pruned an unreachable branch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
