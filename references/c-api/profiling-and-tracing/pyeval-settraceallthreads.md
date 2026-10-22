# void PyEval_SetTraceAllThreads(Py_tracefunc func, PyObject *obj)

void PyEval_SetTraceAllThreads(Py_tracefunc func, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Resembles `PyEval_SetTrace()`, except it installs the tracing function across every running thread of the current interpreter rather than on the current thread alone.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller.

Mirroring `PyEval_SetTrace()`, this call disregards any exception thrown while it installs the trace functions throughout the threads.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytrace-call-to-pyeval-settrace.md) · [Following source contract](pyreftracer-create-to-pyreftracer-gettracer.md)
