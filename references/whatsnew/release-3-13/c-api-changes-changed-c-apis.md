# What's New In Python 3.13 / C API Changes / Changed C APIs — sys

### Changed C APIs

- For [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) and [`PyArg_VaParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_VaParseTupleAndKeywords), the *keywords* parameter has shifted away from char** to type char *const* under C and const char *const* under C++. Within C++, this lets the functions accept arguments typed const char *const*, const char**, or char *const* with no explicit cast required. Within C, only char *const* arguments are accepted by the functions. The [`PY_CXX_CONST`](https://docs.python.org/3.14/c-api/arg.html#c.PY_CXX_CONST) macro provides a way to override this. (Contributed by Serhiy Storchaka in [gh-65210](https://github.com/python/cpython/issues/65210).)

- [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) has gained the ability to handle keyword parameter names that are not ASCII. (Contributed by Serhiy Storchaka in [gh-110815](https://github.com/python/cpython/issues/110815).)

- The `PyCode_GetFirstFree()` function has shifted into unstable API territory and now carries the name [`PyUnstable_Code_GetFirstFree()`](https://docs.python.org/3.14/c-api/code.html#c.PyUnstable_Code_GetFirstFree). (Contributed by Bogdan Romanyuk in [gh-115781](https://github.com/python/cpython/issues/115781).)

- The [`PyDict_GetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItem), [`PyDict_GetItemString()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemString), [`PyMapping_HasKey()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKey), [`PyMapping_HasKeyString()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKeyString), [`PyObject_HasAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttr), [`PyObject_HasAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttrString), and [`PySys_GetObject()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_GetObject) functions, each of which wipes every error that surfaced during the call, will from now on surface such errors by way of [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook). Swapping them for other functions as the documentation advises is an option. (Contributed by Serhiy Storchaka in [gh-106672](https://github.com/python/cpython/issues/106672).)

- Add handling for the `%T`, `%#T`, `%N` and `%#N` formats inside [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat):

  - `%T`: Get the fully qualified name of an object type

  - `%#T`: As above, but use a colon as the separator

  - `%N`: Get the fully qualified name of a type

  - `%#N`: As above, but use a colon as the separator

Consult [**PEP 737**](https://peps.python.org/pep-0737/) for further detail. (Contributed by Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696).)

- Defining the `PY_SSIZE_T_CLEAN` macro ahead of bringing in `Python.h` is no longer necessary when `#` formats appear in [format codes](https://docs.python.org/3.14/c-api/arg.html#arg-parsing-string-and-buffers). Every API that accepts the format codes relies on `Py_ssize_t` for `#` formats throughout. (Contributed by Inada Naoki in [gh-104922](https://github.com/python/cpython/issues/104922).)

- When Python is compiled in [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) or [`with assertions`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-assertions), both [`PyTuple_SET_ITEM()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SET_ITEM) and [`PyList_SET_ITEM()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SET_ITEM) will from now on validate the index argument by way of an assertion. (Contributed by Victor Stinner in [gh-106168](https://github.com/python/cpython/issues/106168).)

[Subject index](INDEX.md) · [Previous source section](audit-tuples-and-c-api-additions.md) · [Next source section](c-api-changes-limited-c-api-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
