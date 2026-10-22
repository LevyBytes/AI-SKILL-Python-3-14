# sys.audit

sys.audit(*event*, **args*)

Fire an auditing event and set off whichever auditing hooks are active. *event* is the string that names the event, while *args* may carry optional arguments conveying further detail about it. For any particular event, the count and types of arguments form a public, stable API and ought not to shift across releases.

As an illustration, one of the auditing events bears the name `os.chdir`. That event takes a single argument named *path*, which will hold the requested new working directory.

`sys.audit()` invokes the auditing hooks already in place, forwarding to each the event name and the arguments, and re-raises the very first exception any hook produces. Generally speaking, an exception raised here should be left unhandled, and the process should stop as fast as it can. That gives hook implementations the choice of how to react to a given event: simply logging it, or canceling the operation by raising.

Hooks get installed by way of the `sys.addaudithook()` or [`PySys_AddAuditHook()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_AddAuditHook) functions.

This function's native counterpart is [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit). Wherever feasible, the native function is the better choice.

Consult the [audit events table](https://docs.python.org/3.14/library/audit_events.html#audit-events) for the complete set of events CPython raises.

Added in version 3.8.

[API family](INDEX.md) · [sys context index](../INDEX.md).
