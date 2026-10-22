# asyncio.eventloop: `loop.remove_signal_handler()`

The supplied callback runs under *loop*, scheduled alongside any other pending callbacks and the coroutines ready to advance on that event loop. In contrast to signal handlers set up via [`signal.signal()`](https://docs.python.org/3.14/library/signal.html#signal.signal), a handler attached through this method may safely touch the event loop.

A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when the signal number cannot be caught or is otherwise invalid. A [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised should configuring the handler fail.

Apply [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) when *callback* needs keyword arguments supplied to it.

As with [`signal.signal()`](https://docs.python.org/3.14/library/signal.html#signal.signal), you must call this from the main thread.

 loop.remove_signal_handler(*sig*)

Drop the registered handler that was watching the *sig* signal.

Yields `True` when an existing handler for that signal was cleared, and `False` when none had been installed for it.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See also

The [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module.

[Subject index](INDEX.md) · [Continue](loop-set-default-executor.md) · [Owning module, declaration or section: Unix signals](loop-add-signal-handler.md) · [Owning module, declaration or section: loop.add_signal_handler](loop-add-signal-handler.md) · [Preceding source contract and version conditions](loop-add-signal-handler.md)
