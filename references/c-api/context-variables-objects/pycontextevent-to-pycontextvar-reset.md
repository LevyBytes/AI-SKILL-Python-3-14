# context variables objects C API: `PyContextEvent`, `PyContextVar_New()`, `PyContextVar_Get()`, `PyContextVar_Set()`, `PyContextVar_Reset()`

type PyContextEvent

Enumeration listing the context object watcher events that may occur:

- `Py_CONTEXT_SWITCHED`: A move has occurred from the [current context](https://docs.python.org/3.14/glossary.html#term-current-context) over to some other context. Whatever the watch callback receives is the [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) object that is now active, or None when nothing is currently in effect.

Added in version 3.14.

 typedef int (*PyContext_WatchCallback)(PyContextEvent event, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Callback function for a context object watcher. Whatever object reaches the callback depends on the event; consult `PyContextEvent` for the specifics.

Should the callback finish with an exception set, it must return `-1`; that exception then gets printed as an unraisable exception by way of [`PyErr_FormatUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_FormatUnraisable). In every other case it should return `0`.

An exception may already be pending when the callback begins. Where that happens, the callback ought to return `0` while leaving that same exception set. So the callback must avoid any other API capable of setting an exception unless it first stashes and clears the exception state, then puts it back before it returns.

Added in version 3.14.

Context variable functions:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyContextVar_New(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *def)

*Return value: New reference.*

Construct a new `ContextVar` object. The *name* parameter serves introspection and debugging needs. The *def* parameter gives a default value for the context variable, or `NULL` when there is no default. Should an error occur, the function returns `NULL`.

 int PyContextVar_Get([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *var, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *default_value, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **value)

Read the value held by a context variable. Returns `-1` when an error happened during the lookup, and `0` when no error happened, regardless of whether a value turned up.

When the context variable is located, *value* will point to it. When the context variable is *not* located, *value* will instead point to:

- *default_value*, if not `NULL`;

- the default value belonging to *var*, when that is not `NULL`;

- `NULL`

Apart from `NULL`, this function hands back a new reference.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyContextVar_Set([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *var, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

*Return value: New reference.*

Assign *value* to *var* within the current context. Hands back a fresh token object recording this change, or `NULL` should an error arise.

 int PyContextVar_Reset([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *var, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *token)

Restore the *var* context variable to the state it held before the `PyContextVar_Set()` call that produced *token* ran. This function returns `0` on success and `-1` on error.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](context-variables-objects.md) · [Previous source contract](pycontexttoken-to-pycontext-clearwatcher.md)
