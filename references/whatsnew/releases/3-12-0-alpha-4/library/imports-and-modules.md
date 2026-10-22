# Python 3.12.0 alpha 4 / library / imports and modules

[gh-97930](https://github.com/python/cpython/issues/97930): A module, not just a package, is now an acceptable anchor for `importlib.resources.files`. Pass a module and resources are located beside it (within the same package or at its root). The argument was renamed from `package` to `anchor`, with a shim kept for callers using the keyword. The new `anchor` argument has also become optional and falls back to the calling module by default.

[gh-99482](https://github.com/python/cpython/issues/99482): Strip `Jython` partial-compatibility code out of several stdlib modules.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
