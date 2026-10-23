# sys.monitoring - Registering and using tools

### Registering and using tools

 sys.monitoring.use_tool_id(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, *name: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*, */*) → [None](https://docs.python.org/3.14/library/constants.html#None)

You must call this before *tool_id* can be put to use. *tool_id* has to fall in the range 0 through 5 inclusive. Raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *tool_id* is already taken.

 sys.monitoring.clear_tool_id(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, */*) → [None](https://docs.python.org/3.14/library/constants.html#None)

Deregister every event and callback function tied to *tool_id*.

 sys.monitoring.free_tool_id(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, */*) → [None](https://docs.python.org/3.14/library/constants.html#None)

Call this once a tool has no further need of *tool_id*. It will invoke `clear_tool_id()` before letting go of *tool_id*.

 sys.monitoring.get_tool(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, */*) → [str](https://docs.python.org/3.14/library/stdtypes.html#str) | [None](https://docs.python.org/3.14/library/constants.html#None)

Hands back the tool's name when *tool_id* is in use, and otherwise hands back `None`. *tool_id* has to fall in the range 0 through 5 inclusive.

The VM treats every ID identically where events are concerned, yet the IDs below are pre-defined to smooth co-operation among tools:

```python
sys.monitoring.DEBUGGER_ID = 0
sys.monitoring.COVERAGE_ID = 1
sys.monitoring.PROFILER_ID = 2
sys.monitoring.OPTIMIZER_ID = 5

```

[Subject index](INDEX.md) · [Previous](tool-identifiers.md) · [Continue](monitoring-branch-call-and-exception-events.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
