# monitoring c api C API: Monitoring state and event-emission functions

type PyMonitoringState

Stands for the state of one event type. You allocate it yourself, but its contents are kept up to date by the monitoring API functions covered below.

Every function below hands back 0 when it succeeds and -1 (with an exception set) when it fails.

For what each event means, refer to [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring).

 int PyMonitoring_FirePyStartEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire a `PY_START` event.

 int PyMonitoring_FirePyResumeEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire a `PY_RESUME` event.

 int PyMonitoring_FirePyReturnEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *retval)

Fire a `PY_RETURN` event.

 int PyMonitoring_FirePyYieldEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *retval)

Fire a `PY_YIELD` event.

 int PyMonitoring_FireCallEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *arg0)

Fire a `CALL` event.

 int PyMonitoring_FireLineEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, int lineno)

Fire a `LINE` event.

 int PyMonitoring_FireJumpEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *target_offset)

Fire a `JUMP` event.

 int PyMonitoring_FireBranchLeftEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *target_offset)

Fire a `BRANCH_LEFT` event.

 int PyMonitoring_FireBranchRightEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *target_offset)

Fire a `BRANCH_RIGHT` event.

 int PyMonitoring_FireCReturnEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *retval)

Fire a `C_RETURN` event.

 int PyMonitoring_FirePyThrowEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire a `PY_THROW` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException)).

 int PyMonitoring_FireRaiseEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire a `RAISE` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException)).

 int PyMonitoring_FireCRaiseEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire a `C_RAISE` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException)).

 int PyMonitoring_FireReraiseEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire a `RERAISE` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException)).

 int PyMonitoring_FireExceptionHandledEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire an `EXCEPTION_HANDLED` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException)).

 int PyMonitoring_FirePyUnwindEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset)

Fire a `PY_UNWIND` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException)).

 int PyMonitoring_FireStopIterationEvent(PyMonitoringState *state, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *codelike, int32_t offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

Fire a `STOP_ITERATION` event. Should `value` already be an instance of [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration), that instance serves directly; if not, a fresh `StopIteration` is built using `value` as its argument.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](monitoring-c-api.md) · [Owning C API section and shared conditions](generating-execution-events.md) · [Following source contract](pymonitoring-enterscope-to-pymonitoring-exitscope.md)
