# Python 3.14.0 alpha 1 / library / importlib resources

[gh-106531](https://github.com/python/cpython/issues/106531): [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources) is brought up to date with [importlib_resources 6.3.2](https://importlib-resources.readthedocs.io/en/latest/history.html#v6-3-2). Among the changes: `MultiplexedPath` now expects `Traversable` paths, deprecating string arguments to `MultiplexedPath`; support arrived for resources inside namespace packages held in zip files; and the `NotADirectoryError` raised when calling files on a subdirectory of a namespace package was repaired.

[gh-123085](https://github.com/python/cpython/issues/123085): For a plain invocation of [`importlib.resources.files()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.files), make certain the calling frame is correctly identified even where `importlib.resources` ships solely as a compiled module with no source present.

[gh-121735](https://github.com/python/cpython/issues/121735): For zip archives, importlib.resources now correctly respects references tied to a module (for instance `files(pkg.mod)`, not merely `files(pkg)`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
