# Heap Types

### Heap Types

By tradition, types written in C are *static*; in other words, `static PyTypeObject` structures declared straight in the code and set up via `PyType_Ready()`.

Types like these are inevitably shared across the whole process. Sharing them among module objects means attending to whatever state they hold or touch. To curb the range of problems, static types stay immutable at the Python level: you cannot, for example, set `str.myattribute = 123`.

**CPython implementation detail:** Sharing genuinely immutable objects across interpreters is acceptable, provided they grant no path to mutable objects. Yet in CPython every Python object carries one mutable implementation detail: its reference count. The GIL guards any change to the refcount. Hence code that shares any Python objects between interpreters quietly leans on CPython’s present, process-wide GIL.

Since they are immutable and process-global, static types have no way to reach ?their? module state. Whenever a method of such a type needs module state, the type has to become a *heap-allocated type*, or *heap type* for short. Those line up more closely with the classes produced by Python's `class` statement.

When writing new modules, defaulting to heap types is a sound guideline.

[Subject index](INDEX.md) · [Previous source context](module-state-access-from-functions.md) · [Following source context](changing-static-types-to-heap-types.md)
