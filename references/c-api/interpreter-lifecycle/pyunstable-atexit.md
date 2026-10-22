# int PyUnstable_AtExit(PyInterpreterState *interp, void (func)(void), void *data)

int PyUnstable_AtExit([PyInterpreterState](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) *interp, void (*func)(void*), void *data)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Sign up an [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) callback against the chosen interpreter *interp*. It resembles [`Py_AtExit()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_AtExit), except it accepts an explicit interpreter plus a data pointer for the callback.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) for *interp* must exist.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-initialize-to-py-bytesmain.md) · [Previous source contract](py-runmain.md) · [Following source contract](cautions-regarding-runtime-finalization.md)
