# Profiling and tracing

## Profiling and tracing

### Profiling and tracing

A measure of low-level support for hooking up profiling and execution-tracing facilities is built into the Python interpreter. Tools for profiling, debugging, and coverage analysis make use of it.

By way of this C interface, profiling or tracing code can dodge the cost of going through Python-level callables and issue a direct C function call instead. None of the facility's core traits have shifted: trace functions can still be set on a per-thread basis, and the elementary events handed to a trace function match those that earlier versions handed to the Python-level trace functions.

 typedef int (*Py_tracefunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *frame, int what, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *arg)

This is the type of trace function you register through `PyEval_SetProfile()` and `PyEval_SetTrace()`. Its opening parameter is whatever object you handed the registration call as *obj*; *frame* names the frame object the event concerns; *what* holds one of the constants `PyTrace_CALL`, `PyTrace_EXCEPTION`, `PyTrace_LINE`, `PyTrace_RETURN`, `PyTrace_C_CALL`, `PyTrace_C_EXCEPTION`, `PyTrace_C_RETURN`, or `PyTrace_OPCODE`; and what *arg* carries follows from the *what* value:

| Value of *what* | Meaning of *arg* |
| --- | --- |
| `PyTrace_CALL` | Always `Py_None`. |
| `PyTrace_EXCEPTION` | Exception information as returned by `sys.exc_info()`. |
| `PyTrace_LINE` | Always `Py_None`. |
| `PyTrace_RETURN` | Value being returned to the caller, or `NULL` if caused by an exception. |
| `PyTrace_C_CALL` | Function object being called. |
| `PyTrace_C_EXCEPTION` | Function object being called. |
| `PyTrace_C_RETURN` | Function object being called. |
| `PyTrace_OPCODE` | Always `Py_None`. |

 int PyTrace_CALL

What *what* holds in a `Py_tracefunc` function as it reports a fresh call into a function or method, or a fresh entry into a generator. Take note that building the iterator for a generator function goes unreported, since no control passes to the Python bytecode within the matching frame.

 int PyTrace_EXCEPTION

What *what* holds in a `Py_tracefunc` function once an exception has gone off. The callback fires carrying this *what* value following any bytecode whose processing leaves the exception set inside the frame then running. The consequence is that, as the exception's propagation unwinds the Python stack, the callback gets invoked on the return into every frame along the way. These events go to trace functions alone; the profiler has no need of them.

 int PyTrace_LINE

The *what* value handed to a `Py_tracefunc` function — though not to a profiling function — when a line-number event is reported. You can switch it off for a given frame by putting [`f_trace_lines`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_lines) at *0* on it.

 int PyTrace_RETURN

The *what* value given to `Py_tracefunc` functions just as a call is on the verge of returning.

 int PyTrace_C_CALL

The *what* value given to `Py_tracefunc` functions right before a C function gets called.

 int PyTrace_C_EXCEPTION

The *what* value given to `Py_tracefunc` functions after a C function has thrown an exception.

 int PyTrace_C_RETURN

The *what* value given to `Py_tracefunc` functions once a C function has come back.

 int PyTrace_OPCODE

The *what* value given to `Py_tracefunc` functions — but not to profiling functions — just before a fresh opcode executes. This one isn't emitted by default: you opt in by setting [`f_trace_opcodes`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_opcodes) to *1* on the frame.

 void PyEval_SetProfile(Py_tracefunc func, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Install *func* as the profiler function. The *obj* parameter rides in as the function's first parameter and can be any Python object or `NULL`. Should the profile function have to keep state, handing *obj* a distinct value per thread gives it a tidy, thread-safe spot to stash that state. Every monitored event triggers the profile function apart from `PyTrace_LINE` `PyTrace_OPCODE` and `PyTrace_EXCEPTION`.

See also the [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) function.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller.

 void PyEval_SetProfileAllThreads(Py_tracefunc func, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Resembles `PyEval_SetProfile()`, except it installs the profile function across every running thread of the current interpreter rather than on the current thread alone.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller.

Mirroring `PyEval_SetProfile()`, this call disregards any exception thrown while it installs the profile functions throughout the threads.

Added in version 3.12.

 void PyEval_SetTrace(Py_tracefunc func, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Install *func* as the tracing function. It runs much like `PyEval_SetProfile()`, save that the tracing function does pick up line-number and per-opcode events while getting nothing tied to calls on C function objects. No trace function registered via `PyEval_SetTrace()` will ever see `PyTrace_C_CALL`, `PyTrace_C_EXCEPTION` or `PyTrace_C_RETURN` come through as the *what* parameter.

See also the [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) function.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller.

[Subject index](INDEX.md) · [Previous source contract](../pickle-buffer-objects/pypicklebuffer-type-to-pypicklebuffer-release.md) · [Following source contract](pyeval-settraceallthreads.md)
