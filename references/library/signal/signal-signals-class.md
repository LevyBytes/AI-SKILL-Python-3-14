# signal: `signal.Signals`

### Module contents

Changed in version 3.5: The constants documented further down — the signal ones (SIG*), the handler ones (`SIG_DFL`, `SIG_IGN`), and the sigmask ones (`SIG_BLOCK`, `SIG_UNBLOCK`, `SIG_SETMASK`) — became [`enums`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum), respectively named `Signals`, `Handlers` and `Sigmasks`. The `getsignal()`, `pthread_sigmask()`, `sigpending()` and `sigwait()` functions hand back readable `enums` in the form of `Signals` objects.

Three enums are declared by the signal module:

 *class *signal.Signals

[`enum.IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) collection of SIG* constants and the CTRL_* constants.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](signals-and-threads.md) · [Continue](signal-handlers-class.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md)
