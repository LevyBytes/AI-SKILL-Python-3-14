# sys.monitoring: Monitoring branch, call and exception event identifiers

### Events

These events are supported:

 sys.monitoring.events.BRANCH_LEFT

A conditional branch goes left.

How to present "left" and "right" branches is left to the tool. There is no promise about which branch counts as "left" and which as "right", other than that it stays consistent for the whole run of the program.

 sys.monitoring.events.BRANCH_RIGHT

A conditional branch goes right.

 sys.monitoring.events.CALL

A call in Python code (event occurs before the call).

 sys.monitoring.events.C_RAISE

An exception thrown out of any callable, Python functions aside (the event lands after the exit).

 sys.monitoring.events.C_RETURN

A return out of any callable, Python functions aside (the event lands after the return).

 sys.monitoring.events.EXCEPTION_HANDLED

An exception is handled.

 sys.monitoring.events.INSTRUCTION

A VM instruction is about to be executed.

 sys.monitoring.events.JUMP

An unconditional jump in the control flow graph is made.

 sys.monitoring.events.LINE

An instruction whose line number differs from that of the instruction before it is on the verge of running.

 sys.monitoring.events.PY_RESUME

A Python function resuming (for generator and coroutine functions), `throw()` calls excepted.

 sys.monitoring.events.PY_RETURN

A return out of a Python function (lands right before the return, with the callee's frame still on the stack).

 sys.monitoring.events.PY_START

A Python function starting (lands right after the call, with the callee's frame on the stack)

 sys.monitoring.events.PY_THROW

A Python function is resumed by a `throw()` call.

 sys.monitoring.events.PY_UNWIND

An exit out of a Python function while exception unwinding is underway. Counted here are exceptions thrown straight inside the function that are permitted to keep propagating.

 sys.monitoring.events.PY_YIELD

A yield out of a Python function (lands right before the yield, with the callee's frame on the stack).

 sys.monitoring.events.RAISE

An exception gets raised, barring the ones that trigger a `STOP_ITERATION` event.

 sys.monitoring.events.RERAISE

An exception gets re-raised, say at the close of a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) block.

[Subject index](INDEX.md) · [Previous](registering-and-using-tools.md) · [Continue](monitoring-iteration-and-event-masks.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
