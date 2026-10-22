# What's new in Python 3.14 / C API changes / Deprecated C APIs

### Deprecated C APIs

- The `Py_HUGE_VAL` macro is now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Rely on `Py_INFINITY` in its place. (Contributed by Sergey B Kirpichev in [gh-120026](https://github.com/python/cpython/issues/120026).)

- The `Py_IS_NAN`, `Py_IS_INFINITY`, and `Py_IS_FINITE` macros are now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Rely on `isnan`, `isinf` and `isfinite`, which `math.h` has offered since C99. (Contributed by Sergey B Kirpichev in [gh-119613](https://github.com/python/cpython/issues/119613).)

- For the `(items)` format unit in [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and other [argument parsing](https://docs.python.org/3.14/c-api/arg.html#arg-parsing) functions, passing non-tuple sequences is now deprecated whenever *items* holds format units that retain a [borrowed buffer](https://docs.python.org/3.14/c-api/arg.html#c-arg-borrowed-buffer) or a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). (Contributed by Serhiy Storchaka in [gh-50333](https://github.com/python/cpython/issues/50333).)

- The `_PyMonitoring_FireBranchEvent` function now carries a deprecation; swap it for calls to [`PyMonitoring_FireBranchLeftEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireBranchLeftEvent) and [`PyMonitoring_FireBranchRightEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireBranchRightEvent).

- The formerly undocumented [`PySequence_In()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_In) function is now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Rely on [`PySequence_Contains()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Contains) in its place. (Contributed by Yuki Kobayashi in [gh-127896](https://github.com/python/cpython/issues/127896).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-removed-c-apis.md) · [Next source section](c-api-removals-scheduled-for-3-15.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md)
