# Python 3.12.0 alpha 1 / c api / interp lifecycle

[gh-93103](https://github.com/python/cpython/issues/93103): Mark the global configuration variables — for example [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag) — as deprecated in the docs, pointing instead to the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API. Victor Stinner authored the patch.

[gh-77782](https://github.com/python/cpython/issues/77782): Deprecate a global configuration variable such as [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag), recommending the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API in its place. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
