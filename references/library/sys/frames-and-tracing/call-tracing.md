# sys.call_tracing

sys.call_tracing(*func*, *args*)

Execute `func(*args)` with tracing turned on. The current tracing state is preserved and then put back afterward. The purpose is invocation from a debugger at a checkpoint, so that some other code can be recursively debugged or profiled.

While a tracing function established by `settrace()` or `setprofile()` runs, tracing is paused to head off infinite recursion. `call_tracing()` makes deliberate recursion of the tracing function possible.

[API family](INDEX.md) · [sys context index](../INDEX.md).
