# Python 3.13.0 beta 1 / core and builtins / sys

[gh-118473](https://github.com/python/cpython/issues/118473): Keep [`sys.set_asyncgen_hooks()`](https://docs.python.org/3.14/library/sys.html#sys.set_asyncgen_hooks) from being left half-set when it raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[gh-117385](https://github.com/python/cpython/issues/117385): Strip the unhandled `PY_MONITORING_EVENT_BRANCH` and `PY_MONITORING_EVENT_EXCEPTION_HANDLED` events out of [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace).

[gh-107674](https://github.com/python/cpython/issues/107674): Markedly raised the performance of [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
