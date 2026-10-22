# Python 3.14.0 beta 1 / core and builtins / exceptions and tracebacks

[gh-131878](https://github.com/python/cpython/issues/131878): Uncaught exceptions arising in the main input loop of the new REPL are now handled.

[gh-129858](https://github.com/python/cpython/issues/129858): An `elif` statement appearing after an `else` block now produces a dedicated error message.

[gh-128398](https://github.com/python/cpython/issues/128398): The error message is improved for the case where an object implementing the synchronous (resp. asynchronous) context manager protocol is entered with [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) (resp. [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)) rather than `with` (resp. `async with`). Bénédikt Tran wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
