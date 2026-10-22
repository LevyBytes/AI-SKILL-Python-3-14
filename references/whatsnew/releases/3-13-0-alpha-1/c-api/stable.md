# Python 3.13.0 alpha 1 / c api / stable

[gh-85283](https://github.com/python/cpython/issues/85283): When the [`Py_LIMITED_API`](https://docs.python.org/3.14/c-api/stable.html#c.Py_LIMITED_API) macro is set, `<Python.h>` now undefines the `Py_BUILD_CORE`, `Py_BUILD_CORE_BUILTIN` and `Py_BUILD_CORE_MODULE` macros. Victor Stinner wrote the patch.

[gh-108634](https://github.com/python/cpython/issues/108634): A Python built using `configure` [`--with-trace-refs`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs) (tracing references) is now compatible with the [Limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api). Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
