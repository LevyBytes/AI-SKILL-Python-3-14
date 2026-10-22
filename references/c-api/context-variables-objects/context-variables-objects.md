# context variables objects C API: Context-variable object API versions and types

## Context Variables Objects

### Context Variables Objects

Added in version 3.7.

Changed in version 3.7.1:

Note

Starting with Python 3.7.1 the signatures of every context variables C API were **changed** so they take [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) pointers rather than `PyContext`, `PyContextVar`, and `PyContextToken`, e.g.:

```c
// in 3.7.0:
PyContext *PyContext_New(void);

// in 3.7.1+:
PyObject *PyContext_New(void);

```

Further details appear in [bpo-34762](https://bugs.python.org/issue?@action=redirect&bpo=34762).

What follows documents the public C API exposed by the [`contextvars`](https://docs.python.org/3.14/library/contextvars.html#module-contextvars) module.

[Subject index](INDEX.md) · [Previous source contract](../concrete-objects-layer/c-api-for-extension-modules.md) · [Following source contract](pycontext.md)
