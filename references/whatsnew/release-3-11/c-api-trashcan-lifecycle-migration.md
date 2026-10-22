# Python 3.11 changes: Trashcan lifecycle and extension porting

### Porting to Python 3.11

- A number of macros were turned into static inline functions so as to sidestep [macro pitfalls](https://gcc.gnu.org/onlinedocs/cpp/Macro-Pitfalls.html). For most users the shift should go unnoticed, given that the replacement functions cast their arguments into the anticipated types to head off compiler warnings stemming from static type checks. That said, once the limited C API is targeted at >=3.11, those casts get skipped, so callers will have to cast arguments into their expected types themselves. Consult [**PEP 670**](https://peps.python.org/pep-0670/) for fuller detail. (Contributed by Victor Stinner and Erlend E. Aasland in [gh-89653](https://github.com/python/cpython/issues/89653).)

- [`PyErr_SetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetExcInfo) makes no further use of the `type` and `traceback` arguments; the interpreter instead works those values out from the exception instance (the `value` argument). All three arguments still have their references stolen by the function. (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

- [`PyErr_GetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetExcInfo) now computes the `type` and `traceback` fields of its result out of the exception instance (the `value` field). (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

- [`_frozen`](https://docs.python.org/3.14/c-api/import.html#c._frozen) gained a new `is_package` field that signals whether the frozen module happens to be a package. Formerly, the marker was a negative value sitting in the `size` field. From now on only non-negative values are valid for `size`. (Contributed by Kumar Aditya in [bpo-46608](https://bugs.python.org/issue?@action=redirect&bpo=46608).)

- [`_PyFrameEvalFunction()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c._PyFrameEvalFunction) now accepts `_PyInterpreterFrame*` as its second parameter, in place of `PyFrameObject*`. Refer to [**PEP 523**](https://peps.python.org/pep-0523/) for fuller detail on working with this function pointer type.

- `PyCode_New()` and `PyCode_NewWithPosOnlyArgs()` now require one extra `exception_table` argument. Steer clear of calling these functions wherever you can. When you need a custom code object, build a code object with the compiler, then obtain a tweaked copy via the `replace` method.

- [`PyCodeObject`](https://docs.python.org/3.14/c-api/code.html#c.PyCodeObject) has dropped the `co_code`, `co_varnames`, `co_cellvars` and `co_freevars` fields. To reach those values from C code instead, call [`PyCode_GetCode()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetCode), [`PyCode_GetVarnames()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetVarnames), [`PyCode_GetCellvars()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetCellvars) and [`PyCode_GetFreevars()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetFreevars) respectively. (Contributed by Brandt Bucher in [bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841) and Ken Jin in [gh-92154](https://github.com/python/cpython/issues/92154) and [gh-94936](https://github.com/python/cpython/issues/94936).)

- The former trashcan macros (`Py_TRASHCAN_SAFE_BEGIN`/`Py_TRASHCAN_SAFE_END`) now carry a deprecation. Swap them out for the newer macros `Py_TRASHCAN_BEGIN` and `Py_TRASHCAN_END`.

Take a tp_dealloc function still relying on the old macros, such as:

```python
static void
mytype_dealloc(mytype *p)
{
    PyObject_GC_UnTrack(p);
    Py_TRASHCAN_SAFE_BEGIN(p);
    ...
    Py_TRASHCAN_SAFE_END
}

```

it ought to move over to the new macros along these lines:

```python
static void
mytype_dealloc(mytype *p)
{
    PyObject_GC_UnTrack(p);
    Py_TRASHCAN_BEGIN(p, mytype_dealloc)
    ...
    Py_TRASHCAN_END
}

```

Be aware that `Py_TRASHCAN_BEGIN` accepts a second argument, which ought to be the deallocation function it sits inside.

If you want the same codebase to keep working on older Python versions, you can declare the following macros and rely on them across the code (credit: these were copied from the `mypy` codebase):

```python
#if PY_VERSION_HEX >= 0x03080000
#  define CPy_TRASHCAN_BEGIN(op, dealloc) Py_TRASHCAN_BEGIN(op, dealloc)
#  define CPy_TRASHCAN_END(op) Py_TRASHCAN_END
#else
#  define CPy_TRASHCAN_BEGIN(op, dealloc) Py_TRASHCAN_SAFE_BEGIN(op)
#  define CPy_TRASHCAN_END(op) Py_TRASHCAN_SAFE_END(op)
#endif

```

- The [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) function now throws an error whenever a type is declared carrying the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag yet lacks a traverse function ([`PyTypeObject.tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse)). (Contributed by Victor Stinner in [bpo-44263](https://bugs.python.org/issue?@action=redirect&bpo=44263).)

-

[Subject index](INDEX.md) · [Previous source section](c-api-changes-new-features.md) · [Next source section](immutable-heap-types-and-vectorcall.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
