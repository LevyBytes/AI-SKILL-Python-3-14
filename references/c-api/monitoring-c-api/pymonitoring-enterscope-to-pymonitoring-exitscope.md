# Managing the Monitoring State

### Managing the Monitoring State

You handle monitoring states by means of monitoring scopes, where a single scope ordinarily lines up with one Python function.

 int PyMonitoring_EnterScope(PyMonitoringState *state_array, uint64_t *version, const uint8_t *event_types, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length)

Enter a monitored scope. The array `event_types` lists the event IDs of every event that the scope is allowed to fire. As an example, a `PY_START` event has the ID `PY_MONITORING_EVENT_PY_START`, a number that equals the base-2 logarithm of `sys.monitoring.events.PY_START`. The array `state_array` carries one monitoring state entry per event in `event_types`; you allocate it, yet `PyMonitoring_EnterScope()` is what fills it in with each event's activation state. How big `event_types` is (and therefore `state_array` as well) comes from `length`.

The `version` argument points at a value that you allocate alongside `state_array` and set to 0 to start with, after which only `PyMonitoring_EnterScope()` writes to it. By means of it the function can tell whether event states have shifted since the last call and bail out fast when they have not.

What count as scopes in this context are lexical scopes — a function, a class, or a method. Each time such a lexical scope is entered, call `PyMonitoring_EnterScope()`. You may re-enter a scope, holding on to the same *state_array* and *version*, in cases like emulating a recursive Python function. Once a code-like's execution is suspended, as happens when emulating a generator, you must leave the scope and then enter it afresh.

The macros for *event_types* are:

| Macro | Event |
| --- | --- |
| PY_MONITORING_EVENT_BRANCH_LEFT | `BRANCH_LEFT` |
| PY_MONITORING_EVENT_BRANCH_RIGHT | `BRANCH_RIGHT` |
| PY_MONITORING_EVENT_CALL | `CALL` |
| PY_MONITORING_EVENT_C_RAISE | `C_RAISE` |
| PY_MONITORING_EVENT_C_RETURN | `C_RETURN` |
| PY_MONITORING_EVENT_EXCEPTION_HANDLED | `EXCEPTION_HANDLED` |
| PY_MONITORING_EVENT_INSTRUCTION | `INSTRUCTION` |
| PY_MONITORING_EVENT_JUMP | `JUMP` |
| PY_MONITORING_EVENT_LINE | `LINE` |
| PY_MONITORING_EVENT_PY_RESUME | `PY_RESUME` |
| PY_MONITORING_EVENT_PY_RETURN | `PY_RETURN` |
| PY_MONITORING_EVENT_PY_START | `PY_START` |
| PY_MONITORING_EVENT_PY_THROW | `PY_THROW` |
| PY_MONITORING_EVENT_PY_UNWIND | `PY_UNWIND` |
| PY_MONITORING_EVENT_PY_YIELD | `PY_YIELD` |
| PY_MONITORING_EVENT_RAISE | `RAISE` |
| PY_MONITORING_EVENT_RERAISE | `RERAISE` |
| PY_MONITORING_EVENT_STOP_ITERATION | `STOP_ITERATION` |

 int PyMonitoring_ExitScope(void)

Leave the most recently entered scope, the one opened by `PyMonitoring_EnterScope()`.

 int PY_MONITORING_IS_INSTRUMENTED_EVENT(uint8_t ev)

Yields true when the event tied to the event ID *ev* is a [local event](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-local).

Added in version 3.13.

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](monitoring-c-api.md) · [Previous source contract](pymonitoringstate-to-pymonitoring-firestopiterationevent.md) · [Following source contract](../the-none-object/py-none-to-py-return-none.md)
