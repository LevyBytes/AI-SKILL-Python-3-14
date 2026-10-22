# Python 3.14.0 alpha 6 / core and builtins / sys

[gh-122029](https://github.com/python/cpython/issues/122029): Neither [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) nor [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) emits a `c_call` event for `INSTRUMENTED_CALL_FUNCTION_EX` when the callable is a method wrapping a C function, since no `c_return` event is produced in that situation.

[gh-130163](https://github.com/python/cpython/issues/130163): Potential crashes tied to attributes of the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module being changed and used at the same time have been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
