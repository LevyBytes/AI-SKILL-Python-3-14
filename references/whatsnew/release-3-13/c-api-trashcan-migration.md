# Python 3.13 changes: Trashcan, frame-local and internal API migration

### Changes in the C API

- `Python.h` has stopped pulling in the `<ieeefp.h>` standard header. That header had been there for the `finite()` function, which the `<math.h>` header now supplies. Include it yourself when you need it. Also drop the `HAVE_IEEEFP_H` macro. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765).)

- `Python.h` no longer brings in these standard header files: `<time.h>`, `<sys/select.h>` and `<sys/time.h>`. Pull them in yourself where required. To illustrate, `<time.h>` offers the `clock()` and `gmtime()` functions, `<sys/select.h>` offers the `select()` function, and `<sys/time.h>` offers the `futimes()`, `gettimeofday()` and `setitimer()` functions. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765).)

- Under Windows, `Python.h` has dropped the `<stddef.h>` standard header file. Include it directly if you need it. It supplies, for instance, the `offsetof()` function plus the `size_t` and `ptrdiff_t` types. Every other platform already required including `<stddef.h>` by hand; the `HAVE_STDDEF_H` macro exists only on Windows. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765).)

- Whenever the [`Py_LIMITED_API`](https://docs.python.org/3.14/c-api/stable.html#c.Py_LIMITED_API) macro is in effect, `<Python.h>` now leaves the `Py_BUILD_CORE`, `Py_BUILD_CORE_BUILTIN` and `Py_BUILD_CORE_MODULE` macros undefined. (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283).)

- The dated trashcan macros `Py_TRASHCAN_SAFE_BEGIN` and `Py_TRASHCAN_SAFE_END` are gone. Swap in the newer macros `Py_TRASHCAN_BEGIN` and `Py_TRASHCAN_END` in their place.

Take a `tp_dealloc` function written with the old macros, like this:

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

ought to be ported over to the new macros like so:

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

Be aware that `Py_TRASHCAN_BEGIN` carries a second argument, which has to be the deallocation function enclosing it. Python 3.8 brought in the new macros, and Python 3.11 deprecated the old ones. (Contributed by Irit Katriel in [gh-105111](https://github.com/python/cpython/issues/105111).)

- Several adjustments to frame-related functions come with PEP 667:

  - What happens when you mutate the dictionary handed back by [`PyEval_GetLocals()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetLocals) within an [optimized scope](https://docs.python.org/3.14/glossary.html#term-optimized-scope) is now different. Fresh dict entries inserted this way become visible *only* to later `PyEval_GetLocals()` calls in that frame, because [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals), [`locals()`](https://docs.python.org/3.14/library/functions.html#locals), and [`FrameType.f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) have stopped sharing the same cached dictionary underneath. Edits to entries for real variable names, as well as names introduced through the write-through proxy interfaces, get clobbered on the next `PyEval_GetLocals()` call in that frame. Which code update to apply hinges on how you were using the function, so see the function's deprecation notice for specifics.

  - Invoking [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals) within an [optimized scope](https://docs.python.org/3.14/glossary.html#term-optimized-scope) now gives back a write-through proxy in place of a snapshot refreshed at loosely defined moments. When a snapshot is what you want, produce one yourself (say, with [`PyDict_Copy()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Copy)), or by reaching for the new [`PyEval_GetFrameLocals()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetFrameLocals) API.

  - `PyFrame_FastToLocals()` and `PyFrame_FastToLocalsWithError()` do nothing anymore. Ever since Python 3.11 first brought in [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals), calling them has been pointless.

  - `PyFrame_LocalsToFast()` likewise does nothing anymore. There's no point calling it now that [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals) hands back a write-through proxy for [optimized scopes](https://docs.python.org/3.14/glossary.html#term-optimized-scope).

- A great many private functions were dropped in Python 3.13. For a number of them, these alternatives serve as replacements:

  - `_PyDict_Pop()`: [`PyDict_Pop()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Pop) or [`PyDict_PopString()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_PopString);

  - `_PyDict_GetItemWithError()`: [`PyDict_GetItemRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemRef);

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](c-api-unraisable-exception-migration.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-13.md)
