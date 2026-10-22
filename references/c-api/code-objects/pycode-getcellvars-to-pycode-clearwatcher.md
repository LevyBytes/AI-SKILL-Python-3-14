# code objects C API: `PyCode_GetCellvars()`, `PyCode_GetFreevars()`, `PyCode_AddWatcher()`, `PyCode_ClearWatcher()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCode_GetCellvars(PyCodeObject *co)

The counterpart of the Python expression `getattr(co, 'co_cellvars')`. It hands back a new reference to a [`PyTupleObject`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTupleObject) that holds the names of those local variables which nested functions refer to. Where something goes wrong, `NULL` comes back and an exception is set.

Added in version 3.11.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCode_GetFreevars(PyCodeObject *co)

The counterpart of the Python expression `getattr(co, 'co_freevars')`. It hands back a new reference to a [`PyTupleObject`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTupleObject) that holds the names of the [free (closure) variables](https://docs.python.org/3.14/glossary.html#term-closure-variable). Where something goes wrong, `NULL` comes back and an exception is set.

Added in version 3.11.

 int PyCode_AddWatcher(PyCode_WatchCallback callback)

Enroll *callback* as a code object watcher tied to the current interpreter. The call gives back an ID you can later feed to `PyCode_ClearWatcher()`. On error (say no watcher IDs remain), it returns `-1` and sets an exception.

Added in version 3.12.

 int PyCode_ClearWatcher(int watcher_id)

Remove the watcher whose *watcher_id* an earlier `PyCode_AddWatcher()` returned for the current interpreter. The call gives back `0` on success, or `-1` plus a set exception on error (for example, when the supplied *watcher_id* was never registered.)

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](code-objects.md) · [Owning structure and shared ABI conditions](pycodeobject-to-pycode-getvarnames.md) · [Following source contract](pycodeevent-to-pycode-optimize.md)
