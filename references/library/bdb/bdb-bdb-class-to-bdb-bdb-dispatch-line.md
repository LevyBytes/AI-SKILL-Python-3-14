# bdb — `bdb` — Debugger framework

*class *bdb.Bdb(*skip=None*, *backend='settrace'*)

The `Bdb` class acts as a generic Python debugger base class.

The particulars of the trace facility are managed by this class; user interaction belongs in a derived class. One example is the standard debugger class ([`pdb.Pdb`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb)).

When supplied, the *skip* argument must be an iterable of glob-style module name patterns. Into frames originating from a module that matches one of these patterns the debugger will not step. Whether a frame counts as originating in a particular module is settled by the `__name__` found in the frame globals.

Which backend `Bdb` uses is set by the *backend* argument. The value may be either `'settrace'` or `'monitoring'`. Backward compatibility is best with `'settrace'`, which relies on [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace). The `'monitoring'` backend draws on the new [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring) added in Python 3.12, and it can be far more efficient since it is able to disable unused events. Though we are working to keep the exact interfaces aligned across both backends, a few differences remain. For better performance, debugger developers are encouraged to reach for the `'monitoring'` backend.

Changed in version 3.1: Added the *skip* parameter.

Changed in version 3.14: Added the *backend* parameter.

Ordinarily the following methods of `Bdb` do not require overriding.

 canonic(*filename*)

Return canonical form of *filename*.

Where real file names are concerned, the canonical form is an operating-system-dependent, [`case-normalized`](https://docs.python.org/3.14/library/os.path.html#os.path.normcase) [`absolute path`](https://docs.python.org/3.14/library/os.path.html#os.path.abspath). Any *filename* bearing angle brackets, like the `"<stdin>"` produced in interactive mode, comes back unchanged.

 start_trace(*self*)

Start tracing. For `'settrace'` backend, this method is equivalent to `sys.settrace(self.trace_dispatch)`

Added in version 3.14.

 stop_trace(*self*)

Stop tracing. For `'settrace'` backend, this method is equivalent to `sys.settrace(None)`

Added in version 3.14.

 reset()

Set the `botframe`, `stopframe`, `returnframe` and `quitting` attributes with values ready to start debugging.

 trace_dispatch(*frame*, *event*, *arg*)

This function is installed as the trace function of debugged frames. Whatever it returns is the new trace function (usually, that is to say, itself).

How a frame gets dispatched is decided by the default implementation according to the kind of event (handed over as a string) that is about to run. *event* can be one of the following:

- `"line"`: A new line of code is going to be executed.

- `"call"`: A function is about to be called, or another code block entered.

- `"return"`: A function or other code block is about to return.

- `"exception"`: An exception has occurred.

- `"c_call"`: A C function is about to be called.

- `"c_return"`: A C function has returned.

- `"c_exception"`: A C function has raised an exception.

Specialized functions (see below) get called for the Python events. Nothing is done for the C events.

The *arg* parameter depends on the previous event.

Consult the documentation for [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) for further detail on the trace function. For further detail on code and frame objects, see [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types).

 dispatch_line(*frame*)

When the debugger should stop on the current line, call the `user_line()` method (which subclasses ought to override). Raise a `BdbQuit` exception whenever the `quitting` flag is set (it may be set from `user_line()`). Give back a reference to the `trace_dispatch()` method so tracing continues within that scope.

[Subject index](INDEX.md) · [Previous](bdb-debugger-framework.md) · [Continue](bdb-bdb-dispatch-call-to-bdb-bdb-set-trace.md) · [Owning module, declaration or section: bdb](bdb-bdbquit.md)
