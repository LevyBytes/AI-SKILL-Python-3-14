# faulthandler - Fault handler state

### Fault handler state

 faulthandler.enable(*file=sys.stderr*, *all_threads=True*, *c_stack=True*)

Turn on the fault handler: register handlers for the [`SIGSEGV`](https://docs.python.org/3.14/library/signal.html#signal.SIGSEGV), [`SIGFPE`](https://docs.python.org/3.14/library/signal.html#signal.SIGFPE), [`SIGABRT`](https://docs.python.org/3.14/library/signal.html#signal.SIGABRT), [`SIGBUS`](https://docs.python.org/3.14/library/signal.html#signal.SIGBUS) and [`SIGILL`](https://docs.python.org/3.14/library/signal.html#signal.SIGILL) signals that emit the Python traceback. With *all_threads* set to `True`, tracebacks are generated for each running thread. If not, only the active thread is dumped.

The *file* has to remain open until the fault handler shuts down: see issue with file descriptors.

When *c_stack* is `True`, the C stack trace follows the Python traceback, except where the system lacks support for it. Consult `dump_c_stack()` for further detail about compatibility.

Changed in version 3.5: This function gained the ability to accept a file descriptor.

Changed in version 3.6: A handler for the Windows exception now gets installed too on Windows.

Changed in version 3.10: Where *all_threads* is true, the dump now notes whether a garbage collector collection is underway.

Changed in version 3.14: When the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) is disabled, only the current thread gets dumped, which heads off any data-race hazard.

Changed in version 3.14: Where *c_stack* is true, the dump now also shows the C stack trace.

 faulthandler.disable()

Turn off the fault handler: remove the signal handlers that `enable()` registered.

 faulthandler.is_enabled()

Report whether the fault handler is active.

[Subject index](INDEX.md) · [Previous](c-stack-compatibility.md) · [Continue](delayed-traceback-dump-and-cancellation.md) · [Owning module, declaration or section: faulthandler](faulthandler-dump-the-python-traceback.md)
