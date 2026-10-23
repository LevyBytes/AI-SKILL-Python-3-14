# sys.monitoring - Per code object events

### Per code object events

Events also admit control on a per code object basis. The functions defined below that take a [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType) should be ready to accept a look-alike object coming from functions not defined in Python (see [Monitoring C API](https://docs.python.org/3.14/c-api/monitoring.html#c-api-monitoring)).

 sys.monitoring.get_local_events(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, *code: [CodeType](https://docs.python.org/3.14/library/types.html#types.CodeType)*, */*) → [int](https://docs.python.org/3.14/library/functions.html#int)

Returns all the local events for *code*

 sys.monitoring.set_local_events(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, *code: [CodeType](https://docs.python.org/3.14/library/types.html#types.CodeType)*, *event_set: [int](https://docs.python.org/3.14/library/functions.html#int)*, */*) → [None](https://docs.python.org/3.14/library/constants.html#None)

Switches on every local event for *code* that is flagged in *event_set*. Raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *tool_id* is not in use.

[Subject index](INDEX.md) · [Previous](setting-events-globally.md) · [Continue](sys-monitoring-disable.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
