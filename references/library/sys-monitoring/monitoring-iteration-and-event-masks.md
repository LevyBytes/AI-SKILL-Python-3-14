# sys.monitoring: `sys.monitoring.events.STOP_ITERATION`, `sys.monitoring.events.NO_EVENTS`

sys.monitoring.events.STOP_ITERATION

An artificial [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) is raised; see the STOP_ITERATION event.

Further events may show up later on.

These events live as attributes of the `sys.monitoring.events` namespace. Every event takes the form of a power-of-2 integer constant. Building a set of events is just a matter of bitwise OR-ing the individual events together. As an example, to call out both the `PY_RETURN` and `PY_START` events, write the expression `PY_RETURN | PY_START`.

 sys.monitoring.events.NO_EVENTS

An alias for `0` so users can do explicit comparisons like:

```python
if get_events(DEBUGGER_ID) == NO_EVENTS:
    ...

```

Setting this event deactivates all events.

[Subject index](INDEX.md) · [Previous](monitoring-branch-call-and-exception-events.md) · [Continue](local-events.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md) · [Owning module, declaration or section: Events](monitoring-branch-call-and-exception-events.md)
