# signal: Console signals, interval timers, masks and signal inspection

signal.CTRL_C_EVENT

The signal that maps to the Ctrl+C keystroke event. The only function that accepts this signal is [`os.kill()`](https://docs.python.org/3.14/library/os.html#os.kill).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.2.

 signal.CTRL_BREAK_EVENT

The signal that maps to the Ctrl+Break keystroke event. The only function that accepts this signal is [`os.kill()`](https://docs.python.org/3.14/library/os.html#os.kill).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.2.

 signal.NSIG

The value sitting one above the highest signal number. To obtain the valid signal numbers, use `valid_signals()`.

 signal.ITIMER_REAL

Counts the interval timer down against wall-clock time, then sends `SIGALRM` once it expires.

 signal.ITIMER_VIRTUAL

Counts the interval timer down solely during the process's own execution, then sends SIGVTALRM once it expires.

 signal.ITIMER_PROF

Counts the interval timer down both while the process runs and while the system runs on the process's behalf. Together with ITIMER_VIRTUAL, this timer commonly serves to profile how much time an application spends across user and kernel space. SIGPROF arrives once it expires.

 signal.SIG_BLOCK

One of the values that the *how* parameter of `pthread_sigmask()` may take, signaling that signals ought to be blocked.

Added in version 3.3.

 signal.SIG_UNBLOCK

One of the values that the *how* parameter of `pthread_sigmask()` may take, signaling that signals ought to be unblocked.

Added in version 3.3.

 signal.SIG_SETMASK

One of the values that the *how* parameter of `pthread_sigmask()` may take, signaling that the signal mask ought to be swapped out.

Added in version 3.3.

A single exception is declared by the `signal` module:

 *exception *signal.ItimerError

Raised to flag an error originating in the underlying `setitimer()` or `getitimer()` implementation. You can anticipate this error whenever a bad interval timer or a negative time gets handed to `setitimer()`. It is a subtype of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Added in version 3.3: In earlier releases this error subtyped [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError); these days that name simply aliases [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

These are the functions that the `signal` module defines:

 signal.alarm(*time*)

When *time* is non-zero, this call asks for a `SIGALRM` signal to reach the process after *time* seconds elapse. It cancels whatever alarm was previously pending (at most one alarm exists at any moment). What comes back is the count of seconds that remained before the prior alarm would have fired. Passing zero for *time* schedules no alarm and cancels any pending one. A return of zero means there's no alarm pending right now.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[alarm(2)](https://manpages.debian.org/alarm(2))* for further information.

 signal.getsignal(*signalnum*)

Hand back the handler presently registered for signal *signalnum*. What you get may be a callable Python object, or alternatively one of the special markers `signal.SIG_IGN`, `signal.SIG_DFL` or [`None`](https://docs.python.org/3.14/library/constants.html#None). In this context, `signal.SIG_IGN` says the signal had been ignored beforehand, `signal.SIG_DFL` says the default handling was in place beforehand, and `None` says the previous handler was set up outside of Python.

 signal.strsignal(*signalnum*)

Hand back a description of signal *signalnum*, for instance “Interrupt” in the case of `SIGINT`. Hands back [`None`](https://docs.python.org/3.14/library/constants.html#None) when *signalnum* carries no description. Throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *signalnum* is not valid.

Added in version 3.8.

 signal.valid_signals()

Hand back the collection of signal numbers that are valid on the current platform. That collection may fall short of `range(1, NSIG)` when the system holds some signals back for its own internal purposes.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](signal-sigpipe-to-signal-sigxcpu.md) · [Continue](signal-pause-to-signal-pthread-sigmask.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md) · [Owning module, declaration or section: Module contents](signal-signals-class.md)
