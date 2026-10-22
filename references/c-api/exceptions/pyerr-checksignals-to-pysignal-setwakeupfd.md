# Signal Handling

### Signal Handling

 int PyErr_CheckSignals()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Service outside interruptions, for instance signals or starting a debugger, whose handling has been postponed until it is safe to run Python code and/or raise exceptions.

As an illustration, hitting Ctrl-C makes a terminal deliver the [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) signal. This function runs the matching Python signal handler, which by default raises the [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception.

Long-running C code ought to invoke `PyErr_CheckSignals()` often enough that the reaction feels instantaneous to people.

The handlers this function presently runs cover:

- Signal handlers, among them Python functions registered by way of the [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module.

Within the main interpreter, signal handlers execute solely on its main thread.

(That history explains the function's name: signals were once the sole mechanism for interrupting the interpreter.)

- Running the garbage collector, if necessary.

- Executing a pending [remote debugger](https://docs.python.org/3.14/howto/remote_debugging.html#remote-debugging) script.

Should any handler raise an exception, return `-1` straight away with that exception set. Whatever interruptions are left over wait to be handled on the following `PyErr_CheckSignals()` call, if that is suitable.

Should every handler complete without error, or should there be no handlers to run, return `0`.

Changed in version 3.12: The garbage collector may now be invoked by this function.

Changed in version 3.14: A remote debugger script may now be run by this function, provided remote debugging is turned on.

 void PyErr_SetInterrupt()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Mimic what happens when a `SIGINT` signal shows up. This amounts to `PyErr_SetInterruptEx(SIGINT)`.

Note

Being async-signal-safe, this function is callable from within a C signal handler and even with no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 int PyErr_SetInterruptEx(int signum)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Mimic what happens when a signal shows up. On the next `PyErr_CheckSignals()` call, the Python signal handler tied to the supplied signal number will run.

C code that arranges its own signal handling, and wants the Python signal handlers fired as expected once an interruption is requested (say, when the user hits Ctrl-C to break off an operation), can invoke this function.

Should the supplied signal not be handled by Python (it was assigned [`signal.SIG_DFL`](https://docs.python.org/3.14/library/signal.html#signal.SIG_DFL) or [`signal.SIG_IGN`](https://docs.python.org/3.14/library/signal.html#signal.SIG_IGN)), it gets ignored.

Should *signum* fall outside the permitted range of signal numbers, `-1` is handed back. Otherwise, `0` is handed back. This function never alters the error indicator.

Note

Being async-signal-safe, this function is callable from within a C signal handler and even with no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Added in version 3.10.

 int PySignal_SetWakeupFd(int fd)

This utility function names a file descriptor onto which the signal number is written as one byte each time a signal arrives. *fd* must be non-blocking. It hands back the file descriptor that was previously in use.

A value of `-1` switches the feature off; that is the starting state. This matches [`signal.set_wakeup_fd()`](https://docs.python.org/3.14/library/signal.html#signal.set_wakeup_fd) in Python, only without any error checking. *fd* should be a valid file descriptor. Only the main thread should make this call.

Changed in version 3.5: Under Windows, socket handles are now supported by the function as well.

[Subject index](INDEX.md) · [Previous source contract](pyerr-getexcinfo-to-pyerr-setexcinfo.md) · [Following source contract](pyerr-newexception-to-pyexceptionclass-name.md)
