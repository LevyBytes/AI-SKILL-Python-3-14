# os: `os.kill()`, `os.killpg()`, `os.nice()`, `os.pidfd_open()`, `os.PIDFD_NONBLOCK`, `os.plock()`

Spawn a child via fork, giving it a freshly created pseudo-terminal as its controlling terminal. The call yields the pair `(pid, fd)`: here *pid* equals `0` inside the child and holds the new child's process id within the parent, while *fd* names the descriptor for the master side of that pseudo-terminal. When you want something more portable, reach for the [`pty`](https://docs.python.org/3.14/library/pty.html#module-pty) module. Should anything go wrong, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.forkpty` with no arguments.

Warning

Under macOS, calling this routine becomes unsafe once it is combined with higher-level system APIs, a category that covers [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) too.

Changed in version 3.8: Invoking `forkpty()` from within a subinterpreter is no longer permitted ([`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised).

Changed in version 3.12: When Python can determine that the current process holds more than one thread, this now emits a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). The fuller account appears under `os.fork()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.kill(*pid*, *sig*, */*)

Deliver signal *sig* to process *pid*. The [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module defines constants for whichever signals the host platform supports.

Windows: [`signal.CTRL_C_EVENT`](https://docs.python.org/3.14/library/signal.html#signal.CTRL_C_EVENT) together with [`signal.CTRL_BREAK_EVENT`](https://docs.python.org/3.14/library/signal.html#signal.CTRL_BREAK_EVENT) are special signals; they may be delivered solely to console processes that share one common console window, such as certain subprocesses. Supplying any other *sig* value makes the TerminateProcess API kill the process outright, and the exit code is set to *sig*.

See also [`signal.pthread_kill()`](https://docs.python.org/3.14/library/signal.html#signal.pthread_kill).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.kill` with arguments `pid`, `sig`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI, not iOS.

Changed in version 3.2: Added Windows support.

 os.killpg(*pgid*, *sig*, */*)

Deliver the signal *sig* to process group *pgid*.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.killpg` with arguments `pgid`, `sig`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not iOS.

 os.nice(*increment*, */*)

Increase the process's "niceness" by *increment*. The new niceness is returned.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.pidfd_open(*pid*, *flags=0*)

Hand back a file descriptor that refers to process *pid*, with *flags* applied. Such a descriptor lets you carry out process management free of races and signals.

Consult the *[pidfd_open(2)](https://manpages.debian.org/pidfd_open(2))* man page for further detail.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 5.3, Android >= [`build-time`](https://docs.python.org/3.14/library/sys.html#sys.getandroidapilevel) API level 31

Added in version 3.9.

 os.PIDFD_NONBLOCK

This flag marks the file descriptor as non-blocking. While the process the descriptor points to has yet to terminate, trying to wait on that descriptor through *[waitid(2)](https://manpages.debian.org/waitid(2))* returns the [`EAGAIN`](https://docs.python.org/3.14/library/errno.html#errno.EAGAIN) error at once instead of blocking.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 5.10

Added in version 3.12.

 os.plock(*op*, */*)

Pin program segments in memory. Which segments end up locked depends on the value of *op* (defined within `<sys/lock.h>`).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not iOS.

[Subject index](INDEX.md) · [Continue](os-popen-to-os-posix-spawn-closefrom.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md) · [Owning module, declaration or section: os.forkpty](os-ex-config-to-os-forkpty.md) · [Preceding source contract and version conditions](os-ex-config-to-os-forkpty.md)
