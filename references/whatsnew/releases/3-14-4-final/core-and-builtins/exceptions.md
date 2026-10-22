# Python 3.14.4 final / core and builtins / exceptions

[gh-141732](https://github.com/python/cpython/issues/141732): Guarantees that the [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) of [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) plus [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup) stays unchanged after the exception sequence originally passed into its constructor is later mutated.

[gh-146250](https://github.com/python/cpython/issues/146250): Plugged a memory leak in [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) that occurred during re-initialization.

[gh-145701](https://github.com/python/cpython/issues/145701): Resolves a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) arising when `__classdict__` or `__conditional_annotations__` lives in a class-scope inlined comprehension. OSS Fuzz reported it in [#491105000](https://issues.oss-fuzz.com/issues/491105000).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
