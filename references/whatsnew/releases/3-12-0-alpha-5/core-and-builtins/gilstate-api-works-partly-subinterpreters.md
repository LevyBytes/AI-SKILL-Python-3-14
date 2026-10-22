# Python 3.12.0 alpha 5 / core and builtins / gilstate api works partly subinterpreters

[gh-59956](https://github.com/python/cpython/issues/59956): The GILState API now works partly with subinterpreters. Until this fix, `PyThreadState_GET()` and `PyGILState_GetThisThreadState()` could drift apart, producing inconsistent behavior and crashes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
