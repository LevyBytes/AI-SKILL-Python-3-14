# synchronization C API: `Py_BEGIN_CRITICAL_SECTION()`, `Py_BEGIN_CRITICAL_SECTION_MUTEX()`, `Py_END_CRITICAL_SECTION()`

### Python critical section API

Sitting above the per-object locks of [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) CPython, the critical section API adds a layer that steers clear of deadlocks. Their purpose is to take the place of leaning on the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock); in Python builds that still carry the global interpreter lock they do nothing at all.

The intended home for critical sections is custom types built in C-API extensions. As a rule you should not pair them with built-in types such as [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) and [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), since the public C-APIs of those types already lean on critical sections under the hood — the one standout being [`PyDict_Next()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Next), where the critical section has to be taken from outside.

The way critical sections dodge deadlocks is by quietly pausing the active ones, which means they do not hand you the exclusive access that conventional locks such as `PyMutex` give. Beginning a critical section takes the object’s per-object lock. Where the code running within that section invokes C-API functions, it may pause the critical section and thereby give up the per-object lock, letting other threads grab the per-object lock for that same object.

There are also variants that take `PyMutex` pointers in place of Python objects. Turn to these when you need to open a critical section but no [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) is around — say, with a C type that neither extends nor wraps `PyObject` yet still has to reach into the C API in ways that could provoke deadlocks.

For situations in which the C macros cannot be reached, the functions and structs that those macros rely on are made public. Confine your use of them to what the supplied macro expansions show. Keep in mind that the size and makeup of these structures may shift in later Python versions.

Note

Whenever an operation has to hold two objects locked together, it must reach for `Py_BEGIN_CRITICAL_SECTION2`. Nesting critical sections *cannot* lock more than a single object at a time, because an inner critical section may pause the outer ones. Locking more than two objects simultaneously is something this API simply does not offer.

A sample of how it is used:

```c
static PyObject *
set_field(MyObject *self, PyObject *value)
{
   Py_BEGIN_CRITICAL_SECTION(self);
   Py_SETREF(self->field, Py_XNewRef(value));
   Py_END_CRITICAL_SECTION();
   Py_RETURN_NONE;
}

```

Within the example just shown, [`Py_SETREF`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_SETREF) invokes [`Py_DECREF`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF), which by way of an object’s deallocation function can run arbitrary code. By letting the runtime briefly pause the critical section whenever the finalizer-triggered code blocks and calls [`PyEval_SaveThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_SaveThread), the critical section API sidesteps the deadlocks that reentrancy and lock ordering might otherwise cause.

 Py_BEGIN_CRITICAL_SECTION(op)

Takes the per-object lock belonging to object *op* and opens a critical section.

Under a free-threaded build, the macro expands into:

```c
{
    PyCriticalSection _py_cs;
    PyCriticalSection_Begin(&_py_cs, (PyObject*)(op))

```

Under the default build, the macro becomes `{`.

Added in version 3.13.

 Py_BEGIN_CRITICAL_SECTION_MUTEX(m)

Locks mutex *m*, then opens a critical section.

Under a free-threaded build, the macro expands into:

```c
{
     PyCriticalSection _py_cs;
     PyCriticalSection_BeginMutex(&_py_cs, m)

```

Be aware that, in contrast to `Py_BEGIN_CRITICAL_SECTION`, the macro applies no cast to its argument — the argument has to be a `PyMutex` pointer.

On a default build, the macro turns into `{`.

Added in version 3.14.

 Py_END_CRITICAL_SECTION()

Closes out the critical section and gives back the per-object lock.

Under a free-threaded build, the macro expands into:

```c
    PyCriticalSection_End(&_py_cs);
}

```

Under the default build, the macro becomes `}`.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source contract](pymutex-to-pymutex-islocked.md) · [Following source contract](py-begin-critical-section2-to-py-end-critical-section2.md)
