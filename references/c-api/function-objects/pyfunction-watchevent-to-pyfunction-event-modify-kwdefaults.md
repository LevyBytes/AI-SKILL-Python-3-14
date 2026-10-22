# function objects C API: `PyFunction_WatchEvent`, `PyFunction_EVENT_CREATE`, `PyFunction_EVENT_DESTROY`, `PyFunction_EVENT_MODIFY_CODE`, `PyFunction_EVENT_MODIFY_DEFAULTS`, `PyFunction_EVENT_MODIFY_KWDEFAULTS`

type PyFunction_WatchEvent

>

The enumeration covering the function watcher events that can occur:

- `PyFunction_EVENT_CREATE`

- `PyFunction_EVENT_DESTROY`

- `PyFunction_EVENT_MODIFY_CODE`

- `PyFunction_EVENT_MODIFY_DEFAULTS`

- `PyFunction_EVENT_MODIFY_KWDEFAULTS`

Added in version 3.12.

 typedef int (*PyFunction_WatchCallback)(PyFunction_WatchEvent event, PyFunctionObject *func, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *new_value)

The type for a function watcher callback function.

When *event* is either `PyFunction_EVENT_CREATE` or `PyFunction_EVENT_DESTROY`, *new_value* comes through as `NULL`. In every other case, *new_value* carries a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) to the incoming value that is on the verge of being written into *func* for the attribute under modification.

While the callback is free to examine *func*, it must leave it unchanged; altering it risks erratic outcomes, infinite recursion among them.

Should *event* be `PyFunction_EVENT_CREATE`, the callback fires once *func* has been completely initialized. In any other situation the callback fires ahead of the change to *func*, leaving *func*'s earlier state open to inspection. The runtime may, where it can, skip building function objects altogether. When that happens, no event goes out. This does open the door to an observable variation in runtime behavior driven by optimization choices, yet it leaves the meaning of the Python code being run untouched.

When *event* is `PyFunction_EVENT_DESTROY`, grabbing a reference within the callback to the function that's about to be torn down brings it back to life, sparing it from being freed right then. Later, once that revived object is destroyed, whatever watcher callbacks are live at that moment fire once more.

Whenever the callback raises an exception, it has to return `-1`; that exception then gets emitted as an unraisable one by way of [`PyErr_WriteUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WriteUnraisable). Failing that, it ought to return `0`.

It's possible that a pending exception is already in place when the callback is entered. Under that circumstance, the callback ought to return `0` while leaving that same exception in place. The implication is that the callback cannot invoke any other API capable of setting an exception unless it first stows and clears the exception state, then puts it back before it returns.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](function-objects.md) · [Previous source contract](pyfunction-getclosure-to-pyfunction-clearwatcher.md)
