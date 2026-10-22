# type objects C API: `PyTypeObject`, `PyType_Type`, `PyType_Check()`, `PyType_CheckExact()`, `PyType_ClearCache()`, `PyType_GetFlags()`, `PyType_GetDict()`, `PyType_Modified()`, `PyType_AddWatcher()`, `PyType_ClearWatcher()`, `PyType_Watch()`

### Type Objects

 type PyTypeObject

* Part of the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable) (as an opaque struct).*

The C-level structure that describes the built-in types.

 PyTypeObject PyType_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This serves as the type object for type objects themselves; on the Python side it is identical to [`type`](https://docs.python.org/3.14/library/functions.html#type).

 int PyType_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Returns a non-zero value when *o* is a type object, which also covers instances of any type derived from the standard type object. Otherwise it returns 0. The call never fails.

 int PyType_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Returns a non-zero value when *o* is a type object that is not itself a subtype of the standard type object. Otherwise it returns 0. The call never fails.

 unsigned int PyType_ClearCache()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Empty the internal lookup cache, then return the current version tag.

 unsigned long PyType_GetFlags(PyTypeObject *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Returns the [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) field of *type*. The intended audience is code built against `Py_LIMITED_API`; while each flag bit stays consistent from one Python release to the next, reaching `tp_flags` directly is outside the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api).

Added in version 3.2.

Changed in version 3.4: The return type is now `unsigned long` rather than `long`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GetDict(PyTypeObject *type)

Returns the internal namespace belonging to the type object; normally this is surfaced only through a read-only proxy ([`cls.__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__)). Use it in place of reaching for [`tp_dict`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dict) directly. Treat the dictionary that comes back as read-only.

The function targets particular embedding and language-binding scenarios in which the dict must be reached directly and indirect routes (for instance the proxy or [`PyObject_GetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetAttr)) fall short.

When extension modules configure their own types, they should keep relying on `tp_dict`, whether directly or indirectly.

Added in version 3.12.

 void PyType_Modified(PyTypeObject *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Discard the internal lookup cache for this type along with every subtype of it. Invoke this whenever you have hand-edited the type's attributes or its base classes.

 int PyType_AddWatcher(PyType_WatchCallback callback)

Sign up *callback* as a watcher of types. The return value is a non-negative integer ID that you supply to later `PyType_Watch()` calls. On failure (for example, when no further watcher IDs remain), it returns `-1` and raises an exception.

In free-threaded builds, `PyType_AddWatcher()` lacks thread safety, so invoke it during start up (ahead of spawning the first thread).

Added in version 3.12.

 int PyType_ClearWatcher(int watcher_id)

Remove the watcher named by *watcher_id* (which an earlier `PyType_AddWatcher()` call handed back). Returns `0` when it succeeds and `-1` on failure (for example, when *watcher_id* was never registered.)

Extensions must never invoke `PyType_ClearWatcher` using a *watcher_id* that was not handed to them by an earlier `PyType_AddWatcher()` call.

Added in version 3.12.

 int PyType_Watch(int watcher_id, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type)

Flag *type* as watched. Whenever `PyType_Modified()` registers a change to *type*, the callback that holds *watcher_id* from `PyType_AddWatcher()` fires. (Across a run of back-to-back modifications to *type*, the callback might fire just once, provided `_PyType_Lookup()` is not invoked on *type* in between; that behavior is an implementation detail and may change.)

Extensions must never invoke `PyType_Watch` using a *watcher_id* that was not handed to them by an earlier `PyType_AddWatcher()` call.

Added in version 3.12.

[Subject index](INDEX.md) · [Following source contract](pytype-unwatch-to-pytype-getqualname.md)
