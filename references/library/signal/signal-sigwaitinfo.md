# signal: `signal.sigwaitinfo()`

signal.sigwaitinfo(*sigset*)

Hold the calling thread's execution until one of the signals named in the signal set *sigset* gets delivered. The function takes the signal in and pulls it off the pending list of signals. Should one of the signals in *sigset* already be pending for the calling thread, the function returns right away carrying details about that signal. The signal handler does not run for the signal thus delivered. The function raises an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) when a signal outside *sigset* interrupts it.

What it returns is an object that stands for the contents of the `siginfo_t` structure — specifically: `si_signo`, `si_code`, `si_errno`, `si_pid`, `si_uid`, `si_status`, `si_band`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[sigwaitinfo(2)](https://manpages.debian.org/sigwaitinfo(2))* for further information.

See also `pause()`, `sigwait()` and `sigtimedwait()`.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](signal-setitimer-to-signal-sigwait.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md) · [Owning module, declaration or section: Module contents](signal-signals-class.md) · [Required continuation of the source contract](signal-sigtimedwait.md)
