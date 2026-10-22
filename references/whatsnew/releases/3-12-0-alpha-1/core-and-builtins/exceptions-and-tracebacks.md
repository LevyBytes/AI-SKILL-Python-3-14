# Python 3.12.0 alpha 1 / core and builtins / exceptions and tracebacks

[gh-97591](https://github.com/python/cpython/issues/97591): A missing incref/decref pair within `Exception.__setstate__()` was repaired. Ofey Chan wrote the patch.

[gh-90997](https://github.com/python/cpython/issues/90997): Compile virtual [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)/[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) blocks so they catch exceptions thrown during [`close()`](https://docs.python.org/3.14/reference/expressions.html#generator.close) or [`throw()`](https://docs.python.org/3.14/reference/expressions.html#generator.throw) calls made through a suspended frame.

[gh-91210](https://github.com/python/cpython/issues/91210): Sharpen the error message shown when a parameter lacking a default value comes after one that has a default, and present that same message even when the non-default/default run sits behind positional-only parameters.

[gh-94215](https://github.com/python/cpython/issues/94215): Resolves a case where line-tracing events that raised exceptions left frames invalid, which could trigger a hard interpreter crash.

[gh-91578](https://github.com/python/cpython/issues/91578): Refreshes the error message used for abstract classes.

[gh-94739](https://github.com/python/cpython/issues/94739): Permit jumping within, out of, and across exception handlers while in the debugger.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
