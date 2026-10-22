# sys.addaudithook

sys.addaudithook(*hook*)

Add the callable *hook* onto the list of auditing hooks active for the current (sub)interpreter.

Whenever an auditing event fires by way of the `sys.audit()` function, every hook is invoked — in registration order — receiving the event name plus the argument tuple. The native hooks registered through [`PySys_AddAuditHook()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_AddAuditHook) run ahead of those added inside the current (sub)interpreter. From there a hook may record the event, throw an exception to halt the operation, or kill the process outright.

Keep in mind that audit hooks exist chiefly to gather data about internal or otherwise hidden behavior, whether originating from Python itself or from libraries written in Python. They are not a fit for building a “sandbox”. Specifically, hostile code can effortlessly switch off or sidestep hooks registered through this function. As a baseline, every security-relevant hook ought to be registered with the C API [`PySys_AddAuditHook()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_AddAuditHook) prior to runtime initialization, and any module that permits arbitrary memory edits (for instance [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes)) should be either stripped out entirely or watched carefully.

The act of calling `sys.addaudithook()` will on its own fire an auditing event called `sys.addaudithook`, carrying no arguments. Should any currently registered hook throw an exception that descends from [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError), the new hook stays unregistered and the exception is swallowed. Consequently, a caller has no way to be sure its hook landed unless it owns every hook already present.

Consult the [audit events table](https://docs.python.org/3.14/library/audit_events.html#audit-events) for the complete set of events CPython raises, and read [**PEP 578**](https://peps.python.org/pep-0578/) for the design discussion that started it.

Added in version 3.8.

Changed in version 3.8.1: An exception that descends from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) yet not from [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is now left unsuppressed.

**CPython implementation detail:** With tracing turned on (refer to `settrace()`), a Python hook is traced only when its callable carries a `__cantrace__` member set to a true value. Failing that, trace functions bypass the hook.

[API family](INDEX.md) · [sys context index](../INDEX.md).
