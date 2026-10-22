# sys.setprofile

sys.setprofile(*profilefunc*)

Set the system’s profile function, which lets you build a Python source code profiler in Python. Turn to the chapter [The Python Profilers](https://docs.python.org/3.14/library/profile.html#profile) to read more about the Python profiler. Invocation of the system’s profile function resembles that of the system’s trace function (see `settrace()`), though it responds to different events; as one example, it does not fire for each executed line of code (only on call and return, although the return event still gets reported even after an exception has been set). The function is thread-specific, yet the profiler cannot detect context switches happening between threads, so applying it where multiple threads exist serves no purpose. Moreover, because its return value goes unused, returning `None` suffices. An error inside the profile function will unset that very function.

Note

The same tracing mechanism backs `setprofile()` as `settrace()`. To trace calls with `setprofile()` from within a tracing function (e.g. at a debugger breakpoint), see `call_tracing()`.

A profile function ought to accept three parameters: *frame*, *event*, and *arg*. Here *frame* denotes the current stack frame. The *event* parameter is a string drawn from `'call'`, `'return'`, `'c_call'`, `'c_return'`, or `'c_exception'`. What *arg* holds hinges on the event type.

Here is what each event signifies:

`'call'`

A function gets called (or another code block is entered). The profile function fires; *arg* is `None`.

`'return'`

A function (or another code block) is on the verge of returning. The profile function fires; *arg* is the value about to be returned, or `None` when the event stems from an exception being raised.

`'c_call'`

A C function is on the verge of being called. This might be an extension function or else a built-in. The *arg* parameter holds the C function object.

`'c_return'`

A C function has returned. The *arg* parameter holds the C function object.

`'c_exception'`

A C function has raised an exception. The *arg* parameter holds the C function object.

Raises an auditing event `sys.setprofile` with no arguments.

[API family](INDEX.md) · [sys context index](../INDEX.md).
