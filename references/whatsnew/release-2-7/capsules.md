# What’s New in Python 2.7 / Capsules - socket, unicodedata

### Capsules

A fresh C datatype, [`PyCapsule`](https://docs.python.org/3.14/c-api/capsule.html#c.PyCapsule), arrives in Python 3.1 to expose a C API from an extension module. At heart a capsule holds a C `void *` pointer and surfaces as a module attribute; the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module's API, for instance, appears as `socket.CAPI`, while [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) publishes `ucnhash_CAPI`. A separate extension can import that module, read its dictionary to grab the capsule object, and then retrieve the `void *` pointer, which typically references an array of pointers aimed at the module's assorted API functions.

A prior type, `PyCObject`, already served this role, but it offers no type safety. Malicious pure-Python code could provoke a segmentation fault by lifting a `PyCObject` out of module A and somehow swapping it in for module B's `PyCObject`. Each capsule carries its own name, and fetching the pointer demands that you supply that name:

```c
void *vtable;

if (!PyCapsule_IsValid(capsule, "mymodule.CAPI") {
        PyErr_SetString(PyExc_ValueError, "argument type invalid");
        return NULL;
}

vtable = PyCapsule_GetPointer(capsule, "mymodule.CAPI");

```

This guarantees that `vtable` refers to exactly what you intended. Were some other capsule handed in, [`PyCapsule_IsValid()`](https://docs.python.org/3.14/c-api/capsule.html#c.PyCapsule_IsValid) would catch the name mismatch and yield false. See [Providing a C API for an Extension Module](https://docs.python.org/3.14/extending/extending.html#using-capsules) to learn more about working with these objects.

Internally Python 2.7 now leans on capsules to expose assorted extension-module APIs, though `PyCObject_AsVoidPtr()` was adjusted to cope with capsules, keeping compile-time compatibility intact with the `PyCObject` interface. Calling `PyCObject_AsVoidPtr()` will trigger a [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning), which stays silent by default.

This was implemented in Python 3.1 and backported into 2.7 by Larry Hastings; the discussion is in [bpo-5630](https://bugs.python.org/issue?@action=redirect&bpo=5630).

[Subject index](INDEX.md) · [Previous source section](build-and-c-api-changes.md) · [Next source section](port-specific-changes-windows.md) · [Release/subject declaration](the-future-for-python-2-x.md)
