# modules C API: `PyModule_AddObjectRef()`, `PyModule_Add()`

### Support functions

The functions below are offered to assist in initializing a module state. They target three settings: a module's execution slots (`Py_mod_exec`); the initialization routine used by legacy [single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#single-phase-initialization); and code that builds modules on the fly.

 int PyModule_AddObjectRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Attach an object to *module* under *name*. This convenience function lends itself to use from a module's initialization function.

When it works, return `0`. When it fails, raise an exception and return `-1`.

Example usage:

```c
static int
add_spam(PyObject *module, int value)
{
    PyObject *obj = PyLong_FromLong(value);
    if (obj == NULL) {
        return -1;
    }
    int res = PyModule_AddObjectRef(module, "spam", obj);
    Py_DECREF(obj);
    return res;
 }

```

For convenience, the function tolerates a `NULL` *value* paired with an exception set. Under that condition, it returns `-1` and simply leaves the raised exception as it stands.

You can also write the example without an explicit check on whether *obj* is `NULL`:

```c
static int
add_spam(PyObject *module, int value)
{
    PyObject *obj = PyLong_FromLong(value);
    int res = PyModule_AddObjectRef(module, "spam", obj);
    Py_XDECREF(obj);
    return res;
 }

```

Here `Py_XDECREF()` ought to take the place of `Py_DECREF()`, given that *obj* may be `NULL`.

Try to keep the count of distinct *name* strings handed to this function low, generally by passing only statically allocated strings as *name*. When names aren't available at compile time, the better route is to invoke [`PyUnicode_FromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromString) plus [`PyObject_SetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetAttr) yourself. Further specifics live at [`PyUnicode_InternFromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternFromString), the routine that the internals may call to build a key object.

Added in version 3.10.

 int PyModule_Add([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Resembles `PyModule_AddObjectRef()`, except it "steals" a reference to *value*. You can pass it the outcome of a function returning a new reference without troubling to inspect that outcome or even stash it in a variable.

Example usage:

```c
if (PyModule_Add(module, "spam", PyBytes_FromString(value)) < 0) {
    goto error;
}

```

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source contract](pymodule-create-to-pymodule-execdef.md) · [Following source contract](pymodule-addobject.md)
