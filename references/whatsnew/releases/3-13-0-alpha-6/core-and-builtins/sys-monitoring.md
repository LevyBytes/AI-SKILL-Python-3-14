# Python 3.13.0 alpha 6 / core and builtins / sys monitoring

[gh-116735](https://github.com/python/cpython/issues/116735): With `INSTRUMENTED_CALL_FUNCTION_EX`, the [`CALL`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-CALL) event now gets `arg0` set to `sys.monitoring.MISSING` rather than `None`.

[gh-116626](https://github.com/python/cpython/issues/116626): Guarantee that `INSTRUMENTED_CALL_FUNCTION_EX` always fires [`CALL`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-CALL)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
