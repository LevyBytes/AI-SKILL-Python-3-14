# What’s New in Python 2.4 / Build and C API Changes

### Build and C API Changes

A selection of the adjustments to Python's build process and its C API follows:

- A trio of handy macros arrived to cover the return values extension functions commonly hand back: [`Py_RETURN_NONE`](https://docs.python.org/3.14/c-api/none.html#c.Py_RETURN_NONE), [`Py_RETURN_TRUE`](https://docs.python.org/3.14/c-api/bool.html#c.Py_RETURN_TRUE), and [`Py_RETURN_FALSE`](https://docs.python.org/3.14/c-api/bool.html#c.Py_RETURN_FALSE). (Contributed by Brett Cannon.)

- One further macro, [`Py_CLEAR`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR), drops the reference count on *obj* and then points *obj* at the null pointer. (Contributed by Jim Fulton.)

- A fresh function, `PyTuple_Pack(N, obj1, obj2, ..., objN)`, assembles tuples out of a variable-length list of Python object arguments. (Contributed by Raymond Hettinger.)

- Another fresh function, `PyDict_Contains(d, k)`, carries out quick dictionary lookups while still letting through any exception thrown along the way. (Contributed by Raymond Hettinger.)

- When handed a float or double argument *X* that happens to be a NaN, the [Py_IS_NAN](https://docs.python.org/3.14/c-api/float.html#c.Py_IS_NAN)(X) macro gives back 1. (Contributed by Tim Peters.)

- By calling the new `PyEval_ThreadsInitialized()` function to learn whether any thread operations have happened yet, C code can skip locking it doesn't need. A false result from that function means no lock work is called for. (Contributed by Nick Coghlan.)

- A fresh function, [`PyArg_VaParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_VaParseTupleAndKeywords), mirrors [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) save that it accepts a `va_list` in place of a series of arguments. (Contributed by Greg Chapman.)

- A new method flag, [`METH_COEXIST`](https://docs.python.org/3.14/c-api/structures.html#c.METH_COEXIST), lets a slot-defined function sit alongside a [`PyCFunction`](https://docs.python.org/3.14/c-api/structures.html#c.PyCFunction) bearing the very same name. For a method like `set.__contains__()` that can cut access time in half. (Contributed by Raymond Hettinger.)

- It's now possible to compile Python with extra profiling of the interpreter itself, meant to help those working on the Python core. Hand `--enable-profiling` to the **configure** script to profile the interpreter via **gprof**, while the `--with-tsc` switch turns on profiling through the Pentium's Time-Stamp-Counter register. Mind that the `--with-tsc` name is a touch off, since the feature serves the PowerPC platform too, even though that architecture doesn't label the register “the TSC register”. (Contributed by Jeremy Hylton.)

- What used to be the `tracebackobject` type now goes by `PyTracebackObject`.

[Subject index](INDEX.md) · [Previous source section](doctest-is-to-a.md) · [Next source section](port-specific-changes.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
