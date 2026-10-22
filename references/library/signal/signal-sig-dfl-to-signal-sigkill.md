# signal: Default signal actions and process-control signal constants

signal.SIG_DFL

One of the pair of standard signal-handling choices; it merely carries out the signal's default behavior. As an illustration, on most systems the default reaction to `SIGQUIT` is to dump core and quit, whereas the default reaction to `SIGCHLD` is just to disregard it.

 signal.SIG_IGN

The second standard signal handler, whose effect is simply to disregard the signal it receives.

 signal.SIGABRT

Abort signal from *[abort(3)](https://manpages.debian.org/abort(3))*.

 signal.SIGALRM

Timer signal from *[alarm(2)](https://manpages.debian.org/alarm(2))*.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 signal.SIGBREAK

Interrupt from keyboard (CTRL + BREAK).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

 signal.SIGBUS

Bus error (bad memory access).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 signal.SIGCHLD

Child process stopped or terminated.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 signal.SIGCLD

Alias to `SIGCHLD`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not macOS.

 signal.SIGCONT

Continue the process if it is currently stopped

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 signal.SIGFPE

Floating-point exception. For example, division by zero.

See also

[`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError) gets raised whenever a division or modulo operation has zero as its second operand.

 signal.SIGHUP

Hangup detected on controlling terminal or death of controlling process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 signal.SIGILL

Illegal instruction.

 signal.SIGINT

Interrupt from keyboard (CTRL + C).

Default action is to raise [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt).

 signal.SIGKILL

Kill signal.

It cannot be caught, blocked, or ignored.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

[Subject index](INDEX.md) · [Previous](signal-sigmasks-class.md) · [Continue](signal-sigpipe-to-signal-sigxcpu.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md) · [Owning module, declaration or section: Module contents](signal-signals-class.md)
