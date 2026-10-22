# What's New In Python 3.10 / C API Changes / Porting to Python 3.10

### Porting to Python 3.10

- The `PY_SSIZE_T_CLEAN` macro must from now on be defined whenever you use [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) formats that rely on `#`: `es#`, `et#`, `s#`, `u#`, `y#`, `z#`, `U#` and `Z#`. Refer to [Parsing arguments and building values](https://docs.python.org/3.14/c-api/arg.html#arg-parsing) and [**PEP 353**](https://peps.python.org/pep-0353/). (Contributed by Victor Stinner in [bpo-40943](https://bugs.python.org/issue?@action=redirect&bpo=40943).)

- Because [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) was turned into the inline static function, any `Py_REFCNT(obj) = new_refcnt` has to become `Py_SET_REFCNT(obj, new_refcnt)`: refer to [`Py_SET_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_SET_REFCNT) (offered since Python 3.9). To keep backward compatibility, you may apply this macro:

```python
#if PY_VERSION_HEX < 0x030900A4
#  define Py_SET_REFCNT(obj, refcnt) ((Py_REFCNT(obj) = (refcnt)), (void)0)
#endif

```

(Contributed by Victor Stinner in [bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573).)

- Invoking [`PyDict_GetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItem) while the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) was not held used to be permitted for historical reasons. That is no longer permitted. (Contributed by Victor Stinner in [bpo-40839](https://bugs.python.org/issue?@action=redirect&bpo=40839).)

- `PyUnicode_FromUnicode(NULL, size)` together with `PyUnicode_FromStringAndSize(NULL, size)` now raise `DeprecationWarning`. Switch to [`PyUnicode_New()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_New) to allocate a Unicode object that has no initial data. (Contributed by Inada Naoki in [bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346).)

- The private `_PyUnicode_Name_CAPI` structure tied to the PyCapsule API `unicodedata.ucnhash_CAPI` was relocated into the internal C API. (Contributed by Victor Stinner in [bpo-42157](https://bugs.python.org/issue?@action=redirect&bpo=42157).)

- [`Py_GetPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPath), [`Py_GetPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPrefix), [`Py_GetExecPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetExecPrefix), [`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath), [`Py_GetPythonHome()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPythonHome) and [`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName) functions now hand back `NULL` if invoked ahead of [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) (that is, before Python has been initialized). Turn to the new [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) API to obtain the [Python Path Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-path-config). (Contributed by Victor Stinner in [bpo-42260](https://bugs.python.org/issue?@action=redirect&bpo=42260).)

- [`PyList_SET_ITEM()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SET_ITEM), [`PyTuple_SET_ITEM()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SET_ITEM) and [`PyCell_SET()`](https://docs.python.org/3.14/c-api/cell.html#c.PyCell_SET) macros are no longer usable as an l-value or r-value. As an example, `x = PyList_SET_ITEM(a, b, c)` and `PyList_SET_ITEM(a, b, c) = x` will now break with a compiler error. This guards against bugs such as the `if (PyList_SET_ITEM (a, b, c) < 0) ...` test. (Contributed by Zackery Spytz and Victor Stinner in [bpo-30459](https://bugs.python.org/issue?@action=redirect&bpo=30459).)

- The non-limited API files `odictobject.h`, `parser_interface.h`, `picklebufobject.h`, `pyarena.h`, `pyctype.h`, `pydebug.h`, `pyfpe.h`, and `pytime.h` were relocated into the `Include/cpython` directory. Do not include these files on their own, since `Python.h` already pulls them in; refer to [Include Files](https://docs.python.org/3.14/c-api/intro.html#api-includes). Should you have included them directly, switch to including `Python.h` instead. (Contributed by Nicholas Sim in [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134).)

- Apply the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) type flag when building immutable type objects. Avoid leaning on [`Py_TPFLAGS_HEAPTYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HEAPTYPE) to determine whether a type object can be mutated; instead test whether `Py_TPFLAGS_IMMUTABLETYPE` is set. (Contributed by Victor Stinner and Erlend E. Aasland in [bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908).)

- The undocumented function `Py_FrozenMain` was dropped from the limited API. That function mainly serves custom builds of Python. (Contributed by Petr Viktorin in [bpo-26241](https://bugs.python.org/issue?@action=redirect&bpo=26241).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-new-features.md) · [Next source section](c-api-changes-deprecated.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-pep-652-maintaining-the-stable-abi.md)
