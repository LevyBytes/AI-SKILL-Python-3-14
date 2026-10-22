# context variables objects C API: Context tokens, copies, entry/exit and watchers

type PyContextToken

The C structure that stands in for a [`contextvars.Token`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Token) object.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyContext_Type

The type object that denotes the *context* type.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyContextVar_Type

The type object that denotes the *context variable* type.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyContextToken_Type

The type object that denotes the *context variable token* type.

Type-check macros:

 int PyContext_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Returns true when *o* has type `PyContext_Type`. *o* must not be `NULL`. This function always succeeds.

 int PyContextVar_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Returns true when *o* has type `PyContextVar_Type`. *o* must not be `NULL`. This function always succeeds.

 int PyContextToken_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Returns true when *o* has type `PyContextToken_Type`. *o* must not be `NULL`. This function always succeeds.

Context object management functions:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyContext_New(void)

*Return value: New reference.*

Build a fresh empty context object. Yields `NULL` should an error arise.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyContext_Copy([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ctx)

*Return value: New reference.*

Make a shallow copy of the supplied *ctx* context object. Yields `NULL` should an error arise.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyContext_CopyCurrent(void)

*Return value: New reference.*

Make a shallow copy of the context belonging to the current thread. Yields `NULL` should an error arise.

 int PyContext_Enter([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ctx)

Install *ctx* as the active context for the running thread. Yields `0` when it succeeds and `-1` on error.

 int PyContext_Exit([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ctx)

Turn off the *ctx* context and bring back the earlier context as the active one for the running thread. Yields `0` when it succeeds and `-1` on error.

 int PyContext_AddWatcher(PyContext_WatchCallback callback)

Sign up *callback* as a context object watcher tied to the current interpreter. Returns an ID that can later be handed to `PyContext_ClearWatcher()`. When something fails (for example, no watcher IDs remain), it returns `-1` and sets an exception.

Added in version 3.14.

 int PyContext_ClearWatcher(int watcher_id)

Remove the watcher named by *watcher_id*, a value previously handed back by `PyContext_AddWatcher()` for the current interpreter. Returns `0` when it succeeds, or `-1` with an exception set on error (for example, when the supplied *watcher_id* was never registered.)

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](context-variables-objects.md) · [Previous source contract](pycontextvar.md) · [Following source contract](pycontextevent-to-pycontextvar-reset.md)
