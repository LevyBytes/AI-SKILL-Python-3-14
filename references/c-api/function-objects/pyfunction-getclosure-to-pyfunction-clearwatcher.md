# function objects C API: Function closures, annotations and watchers

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GetClosure([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

Give back the closure bound to the function object *op*. What you get is either `NULL` or a tuple of cell objects.

 int PyFunction_SetClosure([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *closure)

Assign the closure tied to the function object *op*. The *closure* argument has to be `Py_None` or a tuple of cell objects.

When it fails, [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is thrown and `-1` comes back.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GetAnnotations([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

Give back the annotations held by the function object *op*. This is either a mutable dictionary or `NULL`.

 int PyFunction_SetAnnotations([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *annotations)

Assign the annotations on the function object *op*. The *annotations* argument has to be a dictionary or `Py_None`.

Upon failure, a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised and the call gives back `-1`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GET_CODE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GET_GLOBALS([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GET_MODULE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GET_DEFAULTS([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GET_KW_DEFAULTS([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GET_CLOSURE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GET_ANNOTATIONS([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

These mirror their `PyFunction_Get*` equivalents, except they skip type checking. Hand them anything that isn't an instance of `PyFunction_Type` and the result is undefined behavior.

 int PyFunction_AddWatcher(PyFunction_WatchCallback callback)

Enroll *callback* as a function watcher tied to the current interpreter. The call yields an ID that you can later feed to `PyFunction_ClearWatcher()`. Where something goes wrong — no watcher IDs left, for instance — it yields `-1` and sets an exception.

Added in version 3.12.

 int PyFunction_ClearWatcher(int watcher_id)

Remove the watcher pinpointed by *watcher_id*, the value `PyFunction_AddWatcher()` handed back earlier for the current interpreter. It yields `0` when it works, or `-1` plus an exception on error — say if the *watcher_id* you gave was never enrolled.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](function-objects.md) · [Owning structure and shared ABI conditions](pyfunctionobject-to-pyfunction-setkwdefaults.md) · [Following source contract](pyfunction-watchevent-to-pyfunction-event-modify-kwdefaults.md)
