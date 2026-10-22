# Python 3.14.0 alpha 5 / library / warnings

[gh-128384](https://github.com/python/cpython/issues/128384): Introduce locking in [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) to head off certain data races under free-threading. Turn `_warnings_runtime_state.mutex` into a recursive mutex and surface it to `warnings` through the `_acquire_lock()` and `_release_lock()` functions. That lock stays held while `filters` and `_filters_version` are being updated.

[gh-129766](https://github.com/python/cpython/issues/129766): A crash in [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) that happened when `_release_lock()` was called with no lock present has been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
