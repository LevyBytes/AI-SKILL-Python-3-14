# system interface C API: `PySys_Audit()`, `PySys_AuditTuple()`, `PySys_AddAuditHook()`

int PySys_Audit(const char *event, const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Fire an auditing event toward any active hooks. Yield zero on success, and a non-zero value with an exception set on failure.

The *event* string argument must not be *NULL*.

Whenever hooks have been registered, *format* together with the remaining arguments serves to assemble a tuple that gets passed along. Setting aside `N`, the very same format characters employed by [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) are usable here. Should the constructed value turn out not to be a tuple, it gets wrapped into a single-element tuple.

The `N` format option is off-limits. Because it consumes a reference, yet nothing makes it possible to tell whether this routine's arguments get consumed, employing it can produce reference leaks.

Bear in mind that `#` format characters should always be handled as [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t), no matter whether `PY_SSIZE_T_CLEAN` was defined.

[`sys.audit()`](https://docs.python.org/3.14/library/sys.html#sys.audit) carries out the equivalent task from Python code.

See also `PySys_AuditTuple()`.

Added in version 3.8.

Changed in version 3.8.2: Mandate [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) where `#` format characters appear. Formerly, a deprecation warning that could not be avoided got raised.

 int PySys_AuditTuple(const char *event, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Comparable to `PySys_Audit()`, though it conveys the arguments as a Python object. *args* has to be a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). When no arguments are to be passed, *args* may be *NULL*.

Added in version 3.13.

 int PySys_AddAuditHook(Py_AuditHookFunction hook, void *userData)

Add the callable *hook* onto the list of active auditing hooks. Yield zero on success and a non-zero value on failure. Once the runtime is initialized, an error is also set on failure. Hooks registered via this API fire for each interpreter the runtime creates.

The *userData* pointer gets passed into the hook function. Because hook functions can be invoked from differing runtimes, this pointer ought not to point directly at Python state.

Calling this routine before [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) is safe. When called after the runtime has initialized, the existing audit hooks are notified and can silently abort the work by throwing an error subclassed from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) (any other errors stay unsilenced).

The hook function is always invoked with an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) by whichever Python interpreter raised the event.

Consult [**PEP 578**](https://peps.python.org/pep-0578/) for a thorough account of auditing. The functions across the runtime and the standard library that raise events appear in the [audit events table](https://docs.python.org/3.14/library/audit_events.html#audit-events). Specifics live in each function’s documentation.

Whenever the interpreter is initialized, this routine fires an auditing event `sys.addaudithook` carrying no arguments. Should any pre-existing hook raise an exception derived from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception), the new hook is left unadded and the exception is cleared. Consequently, callers cannot presume their hook was added unless they govern all the existing hooks.

 typedef int (*Py_AuditHookFunction)(const char *event, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, void *userData)

The type that the hook function takes. *event* is the C string event argument handed to `PySys_Audit()` or `PySys_AuditTuple()`. *args* is guaranteed to be a [`PyTupleObject`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTupleObject). *userData* is the argument that was handed to PySys_AddAuditHook().

Added in version 3.8.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pysys-getobject-to-pysys-getxoptions.md) · [Following source contract](py-fatalerror-to-py-atexit.md)
