# Reflection

## Reflection

### Reflection

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_GetBuiltins(void)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Deprecated since version 3.13: Use `PyEval_GetFrameBuiltins()` instead.

Hand back a dictionary holding the builtins of the frame currently executing, or those of the thread state's interpreter when no frame is executing.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_GetLocals(void)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Deprecated since version 3.13: Either reach for `PyEval_GetFrameLocals()`, which reproduces what invoking [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) from Python code does, or alternatively invoke [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals) against the value returned by `PyEval_GetFrame()` so as to read the [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) attribute on the frame now running.

Hand back a mapping that exposes the local variables of the frame currently executing, or `NULL` when no frame is executing.

Consult [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) for specifics on the mapping handed back at various scopes.

Because this function yields a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference), the dictionary produced for [optimized scopes](https://docs.python.org/3.14/glossary.html#term-optimized-scope) gets cached on the frame object and stays alive for as long as that frame object does. In contrast to `PyEval_GetFrameLocals()` and [`locals()`](https://docs.python.org/3.14/library/functions.html#locals), repeated calls to this function from within the same frame revise the cached dictionary's contents to mirror shifts in the local variables, rather than producing a fresh snapshot.

Changed in version 3.13: Under [**PEP 667**](https://peps.python.org/pep-0667/), the shared cache dictionary is no longer consulted by [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals), [`locals()`](https://docs.python.org/3.14/library/functions.html#locals), or [`FrameType.f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals). The [What's New entry](https://docs.python.org/3.14/whatsnew/3.13.html#whatsnew313-locals-semantics) supplies further specifics.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_GetGlobals(void)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Deprecated since version 3.13: Use `PyEval_GetFrameGlobals()` instead.

Hand back a dictionary holding the global variables of the frame currently executing, or `NULL` when no frame is executing.

 [PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *PyEval_GetFrame(void)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state)'s frame, which comes out `NULL` when no frame is executing.

See also [`PyThreadState_GetFrame()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetFrame).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_GetFrameBuiltins(void)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Hand back a dictionary holding the builtins of the frame currently executing, or those of the thread state's interpreter when no frame is executing.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_GetFrameLocals(void)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Hand back a dictionary holding the local variables of the frame currently executing, or `NULL` when no frame is executing. This matches calling [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) within Python code.

To reach [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) on the current frame without taking a separate snapshot under [optimized scopes](https://docs.python.org/3.14/glossary.html#term-optimized-scope), call [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals) on the result of `PyEval_GetFrame()`.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyEval_GetFrameGlobals(void)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Hand back a dictionary holding the global variables of the frame currently executing, or `NULL` when no frame is executing. This matches calling [`globals()`](https://docs.python.org/3.14/library/functions.html#globals) within Python code.

Added in version 3.13.

 const char *PyEval_GetFuncName([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *func)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the name of *func* when it is a function, class or instance object; otherwise hand back the name of *func*'s type.

 const char *PyEval_GetFuncDesc([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *func)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a description string keyed to the type of *func*. Possible results take in "()" for functions and methods, " constructor", " instance", and " object". Joined onto the output of `PyEval_GetFuncName()`, the whole forms a description of *func*.

[Subject index](INDEX.md) · [Previous source contract](../reference-counting/py-setref-to-py-xsetref.md)
