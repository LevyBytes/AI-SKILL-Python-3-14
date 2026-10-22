# Python 3.13.0 alpha 1 / core and builtins / trace refs builds with trace refs had crashing combined isolated subinterpreters

[gh-107080](https://github.com/python/cpython/issues/107080): Trace refs builds (`--with-trace-refs`) had been crashing when combined with isolated subinterpreters. The offending global state was isolated to each interpreter. Beyond removing the crashes, the change has no other user-visible effect.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
