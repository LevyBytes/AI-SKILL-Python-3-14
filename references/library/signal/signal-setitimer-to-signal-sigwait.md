# signal: `signal.setitimer()`, `signal.getitimer()`, `signal.set_wakeup_fd()`, `signal.siginterrupt()`, `signal.signal()`, `signal.sigpending()`, `signal.sigwait()`

signal.setitimer(*which*, *seconds*, *interval=0.0*)

Arm the chosen interval timer (one among `signal.ITIMER_REAL`, `signal.ITIMER_VIRTUAL` or `signal.ITIMER_PROF`), named by *which*, to go off after *seconds* (a float works here, unlike with `alarm()`) and from then on every *interval* seconds (whenever *interval* is non-zero). You disarm the timer named by *which* by giving *seconds* a value of zero.

The moment an interval timer goes off, a signal heads to the process. Which signal that is depends on which timer fired; `signal.ITIMER_REAL` produces `SIGALRM`, `signal.ITIMER_VIRTUAL` produces `SIGVTALRM`, and `signal.ITIMER_PROF` produces `SIGPROF`.

The old values are returned as a tuple: (delay, interval).

Handing over an invalid interval timer triggers an `ItimerError`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 signal.getitimer(*which*)

Hand back the current value of the interval timer named by *which*.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 signal.set_wakeup_fd(*fd*, ***, *warn_on_full_buffer=True*)

Point the wakeup file descriptor at *fd*. Whenever a signal arrives for which your program has registered a signal handler, that signal's number gets written as one byte into the fd. Where you've registered no signal handler for the signals you care about, nothing at all gets written to the wakeup fd. A library can take advantage of this to wake up a poll or select call, which lets the signal be processed in full.

What comes back is the prior wakeup fd (or -1 when file descriptor wakeup was off). Setting *fd* to -1 turns file descriptor wakeup off. When it isn't -1, *fd* has to be non-blocking. The library bears responsibility for clearing any bytes out of *fd* before it calls poll or select once more.

While threads are turned on, only the main thread of the main interpreter may invoke this function; trying to invoke it from any other thread triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception.

This function is typically used in one of two ways. Both approaches use the fd to wake up when a signal lands, but they part ways over how each works out *which* signal or signals landed.

The first approach has us pull the data out of the fd's buffer, where the byte values then tell you the signal numbers. It's straightforward, though now and then it hits a snag: the fd usually carries only so much buffer space, and when signals pile up too fast, the buffer can fill, and a few signals may get dropped. Going this route, you ought to set `warn_on_full_buffer=True`, which will at the very least print a warning to stderr whenever signals are dropped.

The second approach has us treat the wakeup fd *only* as a wakeup mechanism, paying no attention to the actual byte values. Here, the one thing we care about is whether the fd's buffer holds anything or not; a full buffer is no cause for concern whatsoever. Going this route, you ought to set `warn_on_full_buffer=False`, so that spurious warning messages don't confuse your users.

Changed in version 3.5: Under Windows, socket handles are supported by the function as well now.

Changed in version 3.7: Added `warn_on_full_buffer` parameter.

 signal.siginterrupt(*signalnum*, *flag*)

Alter the system-call restart behavior: when *flag* is [`False`](https://docs.python.org/3.14/library/constants.html#False), system calls get restarted after being interrupted by signal *signalnum*; otherwise such system calls are interrupted. Returns nothing.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[siginterrupt(3)](https://manpages.debian.org/siginterrupt(3))* for further information.

Bear in mind that registering a signal handler via `signal()` reverts the restart behavior to interruptible, since it implicitly calls `siginterrupt()` with a true *flag* value for that signal.

 signal.signal(*signalnum*, *handler*)

Assign the handler for signal *signalnum* to be the function *handler*. *handler* may be a callable Python object that takes two arguments (described below), or else one of the special markers `signal.SIG_IGN` or `signal.SIG_DFL`. What comes back is the previous signal handler (refer to the `getsignal()` description above). (Consult the Unix man page *[signal(2)](https://manpages.debian.org/signal(2))* for further information.)

While threads are turned on, only the main thread of the main interpreter may invoke this function; trying to invoke it from any other thread triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception.

The *handler* receives two arguments: the signal number along with the current stack frame (`None` or a frame object; for a rundown on frame objects, consult the [description in the type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) or read the attribute descriptions in the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module).

On Windows, `signal()` can only be called with `SIGABRT`, `SIGFPE`, `SIGILL`, `SIGINT`, `SIGSEGV`, `SIGTERM`, or `SIGBREAK`. Anything else triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Remember that systems differ in which signal names they define; an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) gets raised when a signal name isn't defined as a `SIG*` module-level constant.

 signal.sigpending()

Inspect the collection of signals awaiting delivery to the calling thread (that is, the ones raised while delivery was blocked). Return the collection of pending signals.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[sigpending(2)](https://manpages.debian.org/sigpending(2))* for further information.

See also `pause()`, `pthread_sigmask()` and `sigwait()`.

Added in version 3.3.

 signal.sigwait(*sigset*)

Hold the calling thread's execution until one of the signals named in the signal set *sigset* gets delivered. The function takes the signal in (pulling it off the pending list of signals) and returns that signal's number.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[sigwait(3)](https://manpages.debian.org/sigwait(3))* for further information.

See also `pause()`, `pthread_sigmask()`, `sigpending()`, `sigwaitinfo()` and `sigtimedwait()`.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](signal-pause-to-signal-pthread-sigmask.md) · [Continue](signal-sigwaitinfo.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md) · [Owning module, declaration or section: Module contents](signal-signals-class.md)
