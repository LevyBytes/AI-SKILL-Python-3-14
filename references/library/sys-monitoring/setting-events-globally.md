# sys.monitoring — Setting events globally

### Setting events globally

Global control over events happens by changing the set of events under observation.

 sys.monitoring.get_events(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, */*) → [int](https://docs.python.org/3.14/library/functions.html#int)

Returns the `int` representing all the active events.

 sys.monitoring.set_events(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, *event_set: [int](https://docs.python.org/3.14/library/functions.html#int)*, */*) → [None](https://docs.python.org/3.14/library/constants.html#None)

Switches on every event flagged in *event_set*. Raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *tool_id* is not in use.

By default no events are active.

[Subject index](INDEX.md) · [Previous](turning-events-on-and-off.md) · [Continue](per-code-object-events.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
