# Python 3.12.0 alpha 1 / core and builtins / saves offset first traceable instruction code object sparing recomputation

[gh-93516](https://github.com/python/cpython/issues/93516): Saves the offset of the first traceable instruction on the code object, sparing a recomputation for every instruction during tracing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
