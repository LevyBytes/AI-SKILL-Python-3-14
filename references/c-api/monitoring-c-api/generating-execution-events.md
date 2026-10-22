# monitoring c api C API: Monitoring event arguments and execution-emulation contract

### Generating Execution Events

With the functions that follow, an extension can raise monitoring events while it emulates running Python code. Every one of them takes a `PyMonitoringState` struct holding terse information on which events are active, together with the event arguments — among them a `PyObject*` standing for the code object, the instruction offset, and at times further, event-specific arguments (consult [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring) for the signatures of the various event callbacks). The `codelike` argument ought to be an instance of [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType) or of some type that stands in for it.

Tracing is switched off by the VM while an event is being fired, which means user code does not have to take care of that itself.

You should not invoke monitoring functions while an exception is set, apart from the ones noted further down as operating on the current exception.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](monitoring-c-api.md) · [Following source contract](pymonitoringstate-to-pymonitoring-firestopiterationevent.md)
