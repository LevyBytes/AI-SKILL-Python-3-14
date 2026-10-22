# bdb — `bdb` — Debugger framework

dispatch_call(*frame*, *arg*)

When the debugger should stop on this function call, call the `user_call()` method (which subclasses ought to override). Raise a `BdbQuit` exception whenever the `quitting` flag is set (it may be set from `user_call()`). Give back a reference to the `trace_dispatch()` method so tracing continues within that scope.

 dispatch_return(*frame*, *arg*)

When the debugger should stop on this function return, call the `user_return()` method (which subclasses ought to override). Raise a `BdbQuit` exception whenever the `quitting` flag is set (it may be set from `user_return()`). Give back a reference to the `trace_dispatch()` method so tracing continues within that scope.

 dispatch_exception(*frame*, *arg*)

When the debugger should stop at this exception, calls the `user_exception()` method (which subclasses ought to override). Raise a `BdbQuit` exception whenever the `quitting` flag is set (it may be set from `user_exception()`). Give back a reference to the `trace_dispatch()` method so tracing continues within that scope.

Ordinarily derived classes leave the following methods alone, but they may override them should they wish to redefine what stopping and breakpoints mean.

 is_skipped_module(*module_name*)

Return `True` if *module_name* matches any skip pattern.

 stop_here(*frame*)

Return `True` if *frame* is below the starting frame in the stack.

 break_here(*frame*)

Return `True` if there is an effective breakpoint for this line.

Verify whether a line or function breakpoint exists and is currently active. Drop temporary breakpoints based on what `effective()` reports.

 break_anywhere(*frame*)

Return `True` if any breakpoint exists for *frame*'s filename.

Derived classes should override these methods to gain control over debugger operation.

 user_call(*frame*, *argument_list*)

Called from `dispatch_call()` if a break might stop inside the called function.

*argument_list* is no longer used and will always be `None`. The argument lingers for backwards compatibility.

 user_line(*frame*)

Called from `dispatch_line()` when either `stop_here()` or `break_here()` returns `True`.

 user_return(*frame*, *return_value*)

Called from `dispatch_return()` when `stop_here()` returns `True`.

 user_exception(*frame*, *exc_info*)

Called from `dispatch_exception()` when `stop_here()` returns `True`.

 do_clear(*arg*)

Govern the way a breakpoint has to be removed whenever it happens to be a temporary one.

Derived classes are required to implement this method.

To affect the stepping state, derived classes and clients may invoke the methods below.

 set_step()

Stop after one line of code.

 set_next(*frame*)

Stop on the next line in or below the given frame.

 set_return(*frame*)

Stop when returning from the given frame.

 set_until(*frame*, *lineno=None*)

Stop once the line whose *lineno* exceeds the current one is reached, or upon returning from the current frame.

 set_trace([*frame*])

Start debugging from *frame*. Where *frame* goes unspecified, debugging begins from the caller's frame.

Changed in version 3.13: `set_trace()` will enter the debugger right away, instead of waiting for the next line of code to run.

[Subject index](INDEX.md) · [Previous](bdb-bdb-class-to-bdb-bdb-dispatch-line.md) · [Continue](bdb-bdb-set-continue-to-bdb-bdb-get-stack.md) · [Owning module, declaration or section: bdb](bdb-bdbquit.md) · [Owning module, declaration or section: bdb.Bdb](bdb-bdb-class-to-bdb-bdb-dispatch-line.md)
