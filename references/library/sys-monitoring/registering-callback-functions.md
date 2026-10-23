# sys.monitoring - Registering callback functions

### Registering callback functions

 sys.monitoring.register_callback(*tool_id: [int](https://docs.python.org/3.14/library/functions.html#int)*, *event: [int](https://docs.python.org/3.14/library/functions.html#int)*, *func: [Callable](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Callable) | [None](https://docs.python.org/3.14/library/constants.html#None)*, */*) → [Callable](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Callable) | [None](https://docs.python.org/3.14/library/constants.html#None)

Registers the callable *func* for the *event* with the given *tool_id*

When some other callback had already been registered for the given *tool_id* and *event*, it gets deregistered and returned. If not, `register_callback()` returns `None`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `sys.monitoring.register_callback` with argument `func`.

To deregister functions, call `sys.monitoring.register_callback(tool_id, event, None)`.

Registering and deregistering callback functions may happen at any moment.

Regardless of whether the event is switched on both globally and locally, callbacks fire only once. Accordingly, if your code might switch an event on for both global and local events, you should write the callback to cope with either trigger.

[Subject index](INDEX.md) · [Previous](sys-monitoring-disable.md) · [Continue](sys-monitoring-missing.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
