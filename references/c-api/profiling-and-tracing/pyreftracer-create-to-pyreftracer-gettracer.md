# Reference tracing

### Reference tracing

Added in version 3.13.

 typedef int (*PyRefTracer)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, int event, void *data)

This is the type of trace function you register by way of `PyRefTracer_SetTracer()`. Its first parameter holds a Python object freshly created (where **event** carries `PyRefTracer_CREATE`) or one on the brink of destruction (where **event** carries `PyRefTracer_DESTROY`). For the **data** argument you get back the opaque pointer that was supplied at the `PyRefTracer_SetTracer()` call.

When a fresh tracing function is registered to supplant the existing one, the trace function is invoked with its object at **NULL** and **event** at `PyRefTracer_TRACKER_REMOVED`. That invocation lands right before the new function takes over.

Added in version 3.13.

 int PyRefTracer_CREATE

The *event* value handed to `PyRefTracer` functions once a Python object has come into being.

 int PyRefTracer_DESTROY

The *event* value handed to `PyRefTracer` functions once a Python object has been torn down.

 int PyRefTracer_TRACKER_REMOVED

The *event* value handed to `PyRefTracer` functions just as the existing tracer is on the point of giving way to a fresh one.

Added in version 3.14.

 int PyRefTracer_SetTracer(PyRefTracer tracer, void *data)

Sign up a reference tracer function. It gets invoked whenever a new Python object is created or an existing one is headed for destruction. Where **data** is given, it has to be an opaque pointer that comes back to you at the moment the tracer function runs. A `0` returns on success; on error an exception is set and `-1` is returned.

Mind that a tracer function **must not** create Python objects within it, or the call turns re-entrant. Likewise the tracer **must not** wipe out any standing exception or raise one. A live [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) is present each time the tracer function fires.

Calling this function demands an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Where some other tracer function was registered beforehand, that prior function is invoked with **event** at `PyRefTracer_TRACKER_REMOVED` right ahead of the new one being registered.

Added in version 3.13.

 PyRefTracer PyRefTracer_GetTracer(void **data)

Retrieve the registered reference tracer function together with the opaque data pointer that was registered at the `PyRefTracer_SetTracer()` call. Where nothing was registered, this returns NULL and leaves the **data** pointer at NULL.

Calling this function demands an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytrace-call-to-pyeval-settrace.md) · [Previous source contract](pyeval-settraceallthreads.md)
