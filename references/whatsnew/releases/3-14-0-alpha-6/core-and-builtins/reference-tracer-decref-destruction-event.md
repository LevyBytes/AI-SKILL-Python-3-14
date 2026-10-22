# Python 3.14.0 alpha 6 / core and builtins / pyreftracer destroy not being dispatched py decref python ceval c fixed

[gh-130382](https://github.com/python/cpython/issues/130382): `PyRefTracer_DESTROY` was not being dispatched from the `Py_DECREF()` in `Python/ceval.c`; that is now fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
