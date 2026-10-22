# dictionaries C API: `PyDict_WatchEvent`

type PyDict_WatchEvent

An enumeration covering the dictionary watcher events that can occur: `PyDict_EVENT_ADDED`, `PyDict_EVENT_MODIFIED`, `PyDict_EVENT_DELETED`, `PyDict_EVENT_CLONED`, `PyDict_EVENT_CLEARED`, or `PyDict_EVENT_DEALLOCATED`.

Added in version 3.12.

 typedef int (*PyDict_WatchCallback)(PyDict_WatchEvent event, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *dict, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *new_value)

Type of a dict watcher callback function.

Where *event* equals `PyDict_EVENT_CLEARED` or `PyDict_EVENT_DEALLOCATED`, both *key* and *new_value* come through as `NULL`. Where *event* is `PyDict_EVENT_ADDED` or `PyDict_EVENT_MODIFIED`, *new_value* holds the fresh value assigned to *key*. And where *event* is `PyDict_EVENT_DELETED`, *key* is on its way out of the dictionary while *new_value* is `NULL`.

A `PyDict_EVENT_CLONED` arises where *dict* started out empty and a second dict is merged into it. So this operation stays efficient, no per-key `PyDict_EVENT_ADDED` events go out here; in their place a lone `PyDict_EVENT_CLONED` fires, with *key* set to the source dictionary.

Your callback is free to examine *dict* yet must never alter it; altering it risks unpredictable behavior, infinite recursion among the possibilities. Steer clear of running Python code from within the callback as well, since that could change the dict as a side effect.

When *event* is `PyDict_EVENT_DEALLOCATED`, grabbing a new reference inside the callback to the dictionary about to be destroyed brings it back to life and spares it from being freed for now. Should that revived object later be destroyed, whatever watcher callbacks are live at that moment fire once more.

Because callbacks run ahead of the reported change to *dict*, you can examine the earlier state of *dict*.

Whenever the callback raises an exception, it has to return `-1`; that exception then gets reported as an unraisable one via [`PyErr_WriteUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WriteUnraisable). In every other case it ought to return `0`.

It can happen that an exception is already pending when the callback is entered. Under that circumstance the callback ought to return `0` while leaving that same exception set. As a consequence, the callback must avoid invoking any other API capable of raising an exception unless it first saves and clears the exception state, then puts it back before returning.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydictobject-to-pydict-copy.md) · [Previous source contract](pydict-update-to-pydict-unwatch.md) · [Following source contract](pydictviewset-check-to-pydictitems-check.md)
