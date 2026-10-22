# sys.monitoring — Disabling events

### Disabling events

 sys.monitoring.DISABLE

A special value a callback function can return so that events for the current code location get disabled.

Returning `sys.monitoring.DISABLE` from a callback function lets you switch off local events at one specific code location. Doing so changes neither which events are set nor any other code locations bound to the same event.

Switching off events at particular locations matters a great deal for high performance monitoring. For instance, a program can run under a debugger at zero overhead provided the debugger switches off all monitoring apart from a handful of breakpoints.

Should `DISABLE` come back from a callback for a global event, the interpreter will raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) at a non-specific location (in other words, with no traceback supplied).

 sys.monitoring.restart_events() → [None](https://docs.python.org/3.14/library/constants.html#None)

Switch back on every event that `sys.monitoring.DISABLE` had disabled, across all tools.

[Subject index](INDEX.md) · [Previous](per-code-object-events.md) · [Continue](registering-callback-functions.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
