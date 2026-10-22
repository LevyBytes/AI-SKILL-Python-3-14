# Using Critical Sections

### Using Critical Sections

When you want to work with critical sections, these are the main APIs:

- [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION) and [`Py_END_CRITICAL_SECTION`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION) - to take a lock on one object

- [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2) and [`Py_END_CRITICAL_SECTION2`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION2) - to lock a pair of objects at once

Always deploy these macros as balanced pairs sitting within one and the same C scope, because each pair opens a fresh local scope of its own. On builds that aren't free-threaded they compile down to nothing, which makes them harmless to drop into code meant to serve both build flavors.

A typical reason to enter a critical section is to hold an object locked while you touch one of its internal attributes. Suppose, for instance, that an extension type carries an internal count field — you could open a critical section around the read or the write of that field:

```c
// read the count, returns new reference to internal count value
PyObject *result;
Py_BEGIN_CRITICAL_SECTION(obj);
result = Py_NewRef(obj->count);
Py_END_CRITICAL_SECTION();
return result;

// write the count, consumes reference from new_count
Py_BEGIN_CRITICAL_SECTION(obj);
obj->count = new_count;
Py_END_CRITICAL_SECTION();

```

[Subject index](INDEX.md) · [Previous source context](what-are-critical-sections.md) · [Following source context](how-critical-sections-work.md)
