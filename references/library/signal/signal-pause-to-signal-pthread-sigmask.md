# signal: `signal.pause()`, `signal.raise_signal()`, `signal.pidfd_send_signal()`, `signal.pthread_kill()`, `signal.pthread_sigmask()`

signal.pause()

Put the process to sleep until some signal shows up; the matching handler then runs. Returns nothing.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[signal(2)](https://manpages.debian.org/signal(2))* for further information.

See also `sigwait()`, `sigwaitinfo()`, `sigtimedwait()` and `sigpending()`.

 signal.raise_signal(*signum*)

Dispatches a signal to the process that called it. Returns nothing.

Added in version 3.8.

 signal.pidfd_send_signal(*pidfd*, *sig*, *siginfo=None*, *flags=0*)

Dispatch signal *sig* to whichever process the file descriptor *pidfd* points at. At present Python offers no support for the *siginfo* parameter; it has to be `None`. The *flags* argument exists to allow for later extensions; as of now no flag values have been defined.

See the *[pidfd_send_signal(2)](https://manpages.debian.org/pidfd_send_signal(2))* man page for more information.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 5.1, Android >= [`build-time`](https://docs.python.org/3.14/library/sys.html#sys.getandroidapilevel) API level 31

Added in version 3.9.

 signal.pthread_kill(*thread_id*, *signalnum*)

Dispatch the signal *signalnum* to the thread *thread_id*, which is some other thread living in the same process as the caller. That target thread may be running any code at all (Python or otherwise). That said, if the target thread happens to be running the Python interpreter, then it's the main thread of the main interpreter that will run the Python signal handlers. So the sole reason to direct a signal at one specific Python thread is to make an in-progress system call bail out with [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError).

To obtain a fitting value for *thread_id*, call [`threading.get_ident()`](https://docs.python.org/3.14/library/threading.html#threading.get_ident) or read the [`ident`](https://docs.python.org/3.14/library/threading.html#threading.Thread.ident) attribute on [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) objects.

When *signalnum* equals 0, nothing gets sent, yet error checking still happens; you can leverage this to test whether the target thread remains alive.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `signal.pthread_kill` with arguments `thread_id`, `signalnum`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[pthread_kill(3)](https://manpages.debian.org/pthread_kill(3))* for further information.

See also [`os.kill()`](https://docs.python.org/3.14/library/os.html#os.kill).

Added in version 3.3.

 signal.pthread_sigmask(*how*, *mask*)

Read and/or modify the signal mask of the thread doing the calling. That mask is the collection of signals whose delivery is presently held back for the caller. Returns the prior signal mask as a set of signals.

How the call behaves hinges on the *how* value, in the following way.

- `SIG_BLOCK`: The resulting set of blocked signals combines the present set with the *mask* argument.

- `SIG_UNBLOCK`: Whatever signals appear in *mask* get taken out of the present set of blocked signals. Trying to unblock a signal that isn't currently blocked is allowed.

- `SIG_SETMASK`: The blocked-signal set is replaced outright by the *mask* argument.

The *mask* parameter holds a set of signal numbers (e.g. {`signal.SIGINT`, `signal.SIGTERM`}). For a complete mask covering every signal, call `valid_signals()`.

By way of illustration, `signal.pthread_sigmask(signal.SIG_BLOCK, [])` retrieves the calling thread's signal mask.

`SIGKILL` and `SIGSTOP` cannot be blocked.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

See the man page *[sigprocmask(2)](https://manpages.debian.org/sigprocmask(2))* and *[pthread_sigmask(3)](https://manpages.debian.org/pthread_sigmask(3))* for further information.

See also `pause()`, `sigpending()` and `sigwait()`.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](signal-ctrl-c-event-to-signal-valid-signals.md) · [Continue](signal-setitimer-to-signal-sigwait.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md) · [Owning module, declaration or section: Module contents](signal-signals-class.md)
