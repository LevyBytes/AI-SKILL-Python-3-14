# Ownership Rules — PyLong_FromLong, Py_BuildValue, PyObject_GetAttrString, PyTuple_GetItem, PyList_GetItem, PyDict_GetItem, PyDict_GetItemString, PyImport_AddModule, Py_INCREF, PyTuple_SetItem, PyList_SetItem, PyDict_SetItem

### 1.10.2. Ownership Rules

Any time an object reference crosses into or out of a function, whether ownership travels along with that reference forms part of the function's interface specification.

The majority of functions returning a reference to an object pass ownership along with it. Most notably, every function whose job is to create a new object — for example [`PyLong_FromLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromLong) and [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) — passes ownership to the recipient. Even when the object isn't truly new, you still gain ownership of a new reference to it. As an example, `PyLong_FromLong()` keeps a cache of popular values and may return a reference to a cached entry.

Plenty of functions that pull objects out of other objects also pass ownership along with the reference — [`PyObject_GetAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetAttrString), for one. Here, though, the situation is murkier, since a few common routines are exceptions: [`PyTuple_GetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_GetItem), [`PyList_GetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItem), [`PyDict_GetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItem), and [`PyDict_GetItemString()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemString) each return references that you borrow from the tuple, list or dictionary.

The function [`PyImport_AddModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AddModule) likewise returns a borrowed reference, even though it might actually create the object it hands back: this works because an owned reference to the object is kept in `sys.modules`.

Whenever you hand an object reference into another function, that function generally borrows the reference from you — should it need to store it, it will call [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) to turn itself into an independent owner. There are precisely two notable exceptions to this rule: [`PyTuple_SetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SetItem) and [`PyList_SetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SetItem). These functions assume ownership of the item passed to them — even on failure! (Note that [`PyDict_SetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetItem) and kin don't assume ownership — they behave "normally.")

Whenever a C function is invoked from Python, it borrows references to its arguments from the caller. Because the caller owns a reference to the object, the borrowed reference's lifetime is assured right up until the function returns. Such a borrowed reference must be converted into an owned reference by calling [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) only when it has to be stored or passed onward.

The object reference handed back from a C function that Python invoked must be an owned reference — ownership moves from the function over to its caller.

### 1.10.3. Thin Ice

[Subject index](INDEX.md) · [Previous source section](reference-counting-in-python-py-incref-py-decref.md) · [Required Borrowed references and implicit interpreter calls continuation](borrowed-references-and-implicit-calls.md)
