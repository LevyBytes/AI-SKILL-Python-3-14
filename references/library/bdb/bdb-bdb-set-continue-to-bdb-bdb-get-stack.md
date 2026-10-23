# bdb`bdb` - Debugger framework

set_continue()

Stop only at breakpoints or once finished. Should no breakpoints exist, set the system trace function to `None`.

 set_quit()

Assign `True` to the `quitting` attribute. On the next call into any one of the `dispatch_*()` methods, this raises `BdbQuit`.

To manipulate breakpoints, derived classes and clients may invoke the methods below. Each of these methods returns a string holding an error message when something has gone wrong, or `None` when everything is fine.

 set_break(*filename*, *lineno*, *temporary=False*, *cond=None*, *funcname=None*)

Set a new breakpoint. Should the *lineno* line be absent from the *filename* supplied as the argument, return an error message. Per the `canonic()` method's description, the *filename* should be in canonical form.

 clear_break(*filename*, *lineno*)

Delete the breakpoints in *filename* and *lineno*. When none were set, return an error message.

 clear_bpbynumber(*arg*)

Delete the breakpoint carrying the index *arg* in the `Breakpoint.bpbynumber`. When *arg* is non-numeric or out of range, return an error message.

 clear_all_file_breaks(*filename*)

Delete all breakpoints in *filename*. When none were set, return an error message.

 clear_all_breaks()

Delete all existing breakpoints. When none were set, return an error message.

 get_bpbynumber(*arg*)

Return a breakpoint named by the given number. When *arg* is a string, it gets converted to a number. When *arg* is a non-numeric string, or when the given breakpoint never existed or has been deleted, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Added in version 3.2.

 get_break(*filename*, *lineno*)

Return `True` if there is a breakpoint for *lineno* in *filename*.

 get_breaks(*filename*, *lineno*)

Return all breakpoints for *lineno* in *filename*, or an empty list when none are set.

 get_file_breaks(*filename*)

Return all breakpoints in *filename*, or an empty list when none are set.

 get_all_breaks()

Return all breakpoints that are set.

To disable and restart events for the sake of better performance, derived classes and clients may invoke the methods below. These methods only work when using the `'monitoring'` backend.

 disable_current_event()

Disable the current event until the next time `restart_events()` is called. This comes in handy whenever the debugger has no interest in the current line.

Added in version 3.14.

 restart_events()

Restart all of the disabled events. This function gets called automatically inside `dispatch_*` methods once the `user_*` methods have been called. Where the `dispatch_*` methods go unoverridden, the disabled events will be restarted following each user interaction.

Added in version 3.14.

To obtain a data structure that represents a stack trace, derived classes and clients may invoke the methods below.

 get_stack(*f*, *t*)

Return both a size and a list of (frame, lineno) tuples making up a stack trace.

The frame called most recently sits last in the list. The size counts the frames lying below the frame from which the debugger was invoked.

[Subject index](INDEX.md) · [Previous](bdb-bdb-dispatch-call-to-bdb-bdb-set-trace.md) · [Continue](bdb-bdb-format-stack-entry-to-bdb-bdb-runcall.md) · [Owning module, declaration or section: bdb](bdb-bdbquit.md) · [Owning module, declaration or section: bdb.Bdb](bdb-bdb-class-to-bdb-bdb-dispatch-line.md)
