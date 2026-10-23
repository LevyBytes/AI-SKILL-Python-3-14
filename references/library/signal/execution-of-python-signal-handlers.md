# signal - Execution of Python signal handlers

### Execution of Python signal handlers

The Python signal handler is never run from within the low-level (C) signal handler itself. What the low-level handler does instead is raise a flag, which then directs the [virtual machine](https://docs.python.org/3.14/glossary.html#term-virtual-machine) to invoke the matching Python signal handler somewhat later (say, at the next [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) instruction). A few consequences follow from this:

- There is little value in trying to trap synchronous faults such as `SIGFPE` or `SIGSEGV` that stem from an illegal operation down in C code. Python hands control back from the signal handler into the C code, which will probably trigger the very same signal once more, so Python seems to lock up. Since Python 3.3, the [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) module is available to report such synchronous faults.

- A heavy computation written entirely in C — think matching a regular expression against a huge chunk of text — can keep going uninterrupted for as long as it likes, no matter which signals show up. Only once that computation wraps up will the Python signal handlers fire.

- Should the handler throw an exception, that exception surfaces “out of thin air” over in the main thread. The note further down covers this.

[Subject index](INDEX.md) · [Previous](general-rules.md) · [Continue](signals-and-threads.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md)
