# Low-level APIs

### Low-level APIs

Every function below has to be invoked only after [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize).

Changed in version 3.7: The [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) now gets initialized by [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize), which additionally establishes an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 PyInterpreterState *PyInterpreterState_New()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a fresh interpreter state object. No [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required, though one may be present if calls to this function need serializing.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.PyInterpreterState_New` with no arguments.

 void PyInterpreterState_Clear(PyInterpreterState *interp)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Wipe every piece of information held in an interpreter state object. The interpreter requires an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.PyInterpreterState_Clear` with no arguments.

 void PyInterpreterState_Delete(PyInterpreterState *interp)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Tear down an interpreter state object. For the target interpreter there **should not** be an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). Beforehand the interpreter state has to have been wiped through an earlier call to `PyInterpreterState_Clear()`.

[Subject index](INDEX.md) · [Previous source contract](pyinterpreterstate-to-pyinterpreterstate-setevalframefunc.md) · [Following source contract](pyinterpreterstate-head-to-pythreadstate-next.md)
