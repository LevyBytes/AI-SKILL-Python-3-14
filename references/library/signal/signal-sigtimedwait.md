# signal: `signal.sigtimedwait()`

Changed in version 3.5: When a signal that lies outside *sigset* breaks into the call and the handler raises nothing, the call is now reattempted automatically (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)).

 signal.sigtimedwait(*sigset*, *timeout*)

Works the same way as `sigwaitinfo()`, except it accepts an extra *timeout* argument that bounds how long it will wait. Supplying `0` for *timeout* makes the call act as a single poll. Should the wait elapse, the return value is [`None`](https://docs.python.org/3.14/library/constants.html#None).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Consult the man page *[sigtimedwait(2)](https://manpages.debian.org/sigtimedwait(2))* if you need more detail.

Related entries: `pause()`, `sigwait()`, and `sigwaitinfo()`.

Added in version 3.3.

Changed in version 3.5: When a signal outside *sigset* interrupts the call and the handler raises nothing, the call is now retried using a freshly computed *timeout* (the reasoning appears in [**PEP 475**](https://peps.python.org/pep-0475/)).

[Subject index](INDEX.md) · [Continue](examples.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md) · [Owning module, declaration or section: Module contents](signal-signals-class.md) · [Owning module, declaration or section: signal.sigwaitinfo](signal-sigwaitinfo.md) · [Preceding source contract and version conditions](signal-sigwaitinfo.md)
