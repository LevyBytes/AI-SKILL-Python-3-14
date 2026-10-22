# synchronization C API: `Py_BEGIN_CRITICAL_SECTION2()`, `Py_BEGIN_CRITICAL_SECTION2_MUTEX()`, `Py_END_CRITICAL_SECTION2()`

Py_BEGIN_CRITICAL_SECTION2(a, b)

Takes the per-object locks of both object *a* and object *b*, then opens a critical section. To head off lock-ordering deadlocks, those locks are taken in a fixed order — the lowest address coming first.

Under a free-threaded build, the macro expands into:

```c
{
    PyCriticalSection2 _py_cs2;
    PyCriticalSection2_Begin(&_py_cs2, (PyObject*)(a), (PyObject*)(b))

```

Under the default build, the macro becomes `{`.

Added in version 3.13.

 Py_BEGIN_CRITICAL_SECTION2_MUTEX(m1, m2)

Locks both mutex *m1* and mutex *m2*, then opens a critical section.

Under a free-threaded build, the macro expands into:

```c
{
     PyCriticalSection2 _py_cs2;
     PyCriticalSection2_BeginMutex(&_py_cs2, m1, m2)

```

Be aware that, in contrast to `Py_BEGIN_CRITICAL_SECTION2`, the macro casts none of its arguments — each argument has to be a `PyMutex` pointer.

On a default build, the macro turns into `{`.

Added in version 3.14.

 Py_END_CRITICAL_SECTION2()

Closes out the critical section and gives back the per-object locks.

Under a free-threaded build, the macro expands into:

```c
    PyCriticalSection2_End(&_py_cs2);
}

```

Under the default build, the macro becomes `}`.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-begin-critical-section-to-py-end-critical-section.md) · [Following source contract](legacy-locking-apis.md)
