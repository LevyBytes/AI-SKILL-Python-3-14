# sys.settrace

sys.settrace(*tracefunc*)

Set the system’s trace function, the hook that lets you implement, in Python, a debugger for Python source code. This function operates per thread; so that a debugger can cope with several threads, it has to register a trace function via `settrace()` for every thread being debugged, or else use [`threading.settrace()`](https://docs.python.org/3.14/library/threading.html#threading.settrace).

A trace function ought to accept three parameters: *frame*, *event*, and *arg*. Here *frame* denotes the [current stack frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects). The *event* parameter is a string drawn from `'call'`, `'line'`, `'return'`, `'exception'` or `'opcode'`. What *arg* holds hinges on the event type.

Each time a new local scope is entered, the trace function fires with its *event* argument set to `'call'`; it ought to hand back a reference to a local trace function that the new scope will use, or `None` if that scope should go untraced.

The local trace function should return a reference to itself, or to a different function that would then serve as the local trace function for the scope.

Should any error arise in the trace function, it will be unset, exactly as though `settrace(None)` had been called.

Note

Tracing is turned off while the trace function runs (e.g. a function set by `settrace()`). For recursive tracing see `call_tracing()`.

Here is what each event signifies:

`'call'`

A function gets called (or another code block is entered). The global trace function fires; *arg* is `None`; the return value names the local trace function.

`'line'`

The interpreter is on the verge of running a new line of code or re-running a loop’s condition. The local trace function fires; *arg* is `None`; the return value names the new local trace function. Consult `Objects/lnotab_notes.txt` for a thorough account of the mechanism. You can switch off per-line events for a frame by assigning [`f_trace_lines`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_lines) the value [`False`](https://docs.python.org/3.14/library/constants.html#False) on that [frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects).

`'return'`

A function (or another code block) is on the verge of returning. The local trace function fires; *arg* is the value about to be returned, or `None` when the event stems from an exception being raised. The trace function’s return value is ignored.

`'exception'`

An exception has occurred. The local trace function fires; *arg* is a tuple `(exception, value, traceback)`; the return value names the new local trace function.

`'opcode'`

The interpreter is on the verge of running a new opcode (consult [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) for opcode details). The local trace function fires; *arg* is `None`; the return value names the new local trace function. Per-opcode events are withheld by default: you must explicitly request them by assigning [`f_trace_opcodes`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_opcodes) the value [`True`](https://docs.python.org/3.14/library/constants.html#True) on the [frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects).

Keep in mind that as an exception propagates down the chain of callers, an `'exception'` event arises at every level.

For finer-grained control, you can install a trace function by assigning `frame.f_trace = tracefunc` directly, instead of depending on it being set indirectly through the return value of an already installed trace function. This is also necessary to activate the trace function on the current frame, something `settrace()` does not do. Note that for any of this to function, a global tracing function has to have been installed with `settrace()` to switch on the runtime tracing machinery, though it does not have to be the identical tracing function (for instance, it might be a lightweight tracing function that merely hands back `None` so as to turn itself off right away on each frame).

For more information on code and frame objects, refer to [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types).

Raises an auditing event `sys.settrace` with no arguments.

**CPython implementation detail:** The `settrace()` function is meant solely for building debuggers, profilers, coverage tools and similar utilities. Its behavior belongs to the implementation platform rather than to the language definition, and as such may not be present in every Python implementation.

Changed in version 3.7: the `'opcode'` event type was introduced; the [`f_trace_lines`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_lines) and [`f_trace_opcodes`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_opcodes) attributes were added to frames

[API family](INDEX.md) · [sys context index](../INDEX.md).
