# code objects C API: `PyCodeEvent`, `PyCode_Optimize()`

type PyCodeEvent

An enumeration spanning the code object watcher events that can occur: - `PY_CODE_EVENT_CREATE` - `PY_CODE_EVENT_DESTROY`

Added in version 3.12.

 typedef int (*PyCode_WatchCallback)(PyCodeEvent event, PyCodeObject *co)

Type of a code object watcher callback function.

Where *event* equals `PY_CODE_EVENT_CREATE`, the callback fires once *co* is fully initialized. In the other case it fires ahead of *co* being destroyed, which leaves room to examine the earlier state of *co*.

Where *event* equals `PY_CODE_EVENT_DESTROY`, grabbing a reference within the callback to the code object on the verge of destruction brings it back to life and keeps it from being freed for now. Should that revived object be destroyed at a later point, whatever watcher callbacks are live then fire once again.

Anyone using this API ought not lean on internal runtime implementation details. Among such details, though not only these, are the precise sequence and timing with which code objects come into being and pass away. Shifts in those details might yield differences a watcher can observe (down to whether a callback fires at all), yet they leave the meaning of the running Python code untouched.

Should the callback raise an exception, returning `-1` is mandatory; that exception is then emitted as an unraisable one through [`PyErr_WriteUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WriteUnraisable). Failing that, it ought to return `0`.

On entry the callback may find an exception already pending. Should that be so, it ought to return `0` and leave the very same exception in place. Practically, this bars the callback from calling any other exception-setting API unless it first preserves and clears the exception state, then reinstates it just before returning.

Added in version 3.12.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCode_Optimize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *code, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *consts, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *names, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *lnotab_obj)

A [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) function that has no effect at all.

Back before Python 3.10, this function used to carry out simple optimizations on a code object.

Changed in version 3.10: This function now does nothing.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](code-objects.md) · [Previous source contract](pycode-getcellvars-to-pycode-clearwatcher.md) · [Following source contract](code-object-flags.md)
