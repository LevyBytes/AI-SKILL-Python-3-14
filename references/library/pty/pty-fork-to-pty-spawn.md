# pty`pty` - Pseudo-terminal utilities

### `pty` - Pseudo-terminal utilities

**Source code:** [Lib/pty.py](https://github.com/python/cpython/tree/3.14/Lib/pty.py)

---

The `pty` module lays out operations for working with the pseudo-terminal idea: launching a separate process and gaining the ability to write to and read from its controlling terminal programmatically.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

How pseudo-terminals get handled leans heavily on the platform. The bulk of testing for this code happened on Linux, FreeBSD, and macOS (it ought to function on other POSIX platforms though it's not been thoroughly tested).

The `pty` module lays out the following functions:

 pty.fork()

Fork. Wire the child's controlling terminal up to a pseudo-terminal. The return value is `(pid, fd)`. Mind that the child receives *pid* 0, and its *fd* is *invalid*. On the parent side the return value is the child's *pid*, while *fd* is a file descriptor wired to the child's controlling terminal (and likewise to the child's standard input and output).

Warning

Under macOS calling this function is unsafe once it's mixed with higher-level system APIs, and that takes in using [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request).

 pty.openpty()

Open a fresh pseudo-terminal pair, reaching for [`os.openpty()`](https://docs.python.org/3.14/library/os.html#os.openpty) where possible, or emulation code on generic Unix systems. Hand back a pair of file descriptors `(master, slave)`, one apiece for the master end and the slave end.

 pty.spawn(*argv*[, *master_read*[, *stdin_read*]])

Spawn a process, and wire its controlling terminal up to the current process's standard io. People often lean on this to fool programs that demand reading from the controlling terminal. The process spawned behind the pty is expected to terminate at some point, and once it does *spawn* will return.

A loop ferries STDIN of the current process across to the child and data arriving from the child over to STDOUT of the current process. The child gets no signal should STDIN of the current process shut down.

The functions *master_read* and *stdin_read* each receive a file descriptor they should read from, and they should invariably hand back a byte string. To force spawn to return ahead of the child process exiting, hand back an empty byte array to flag end of file.

Each function's default implementation reads and hands back up to 1024 bytes per call. The *master_read* callback receives the pseudoterminal's master file descriptor to pull output from the child process, while *stdin_read* receives file descriptor 0, to read from the parent process's standard input.

Handing back an empty byte string from either callback reads as an end-of-file (EOF) condition, and that callback won't be called thereafter. Should *stdin_read* flag EOF, the controlling terminal can no longer talk to the parent process OR the child process. Barring a child process that quits with no input, *spawn* then loops forever. Should *master_read* flag EOF the same behavior follows (on linux at least).

Hand back the exit status value from [`os.waitpid()`](https://docs.python.org/3.14/library/os.html#os.waitpid) on the child process.

[`os.waitstatus_to_exitcode()`](https://docs.python.org/3.14/library/os.html#os.waitstatus_to_exitcode) serves to turn the exit status into an exit code.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `pty.spawn` with argument `argv`.

Changed in version 3.4: `spawn()` from now on hands back the status value that [`os.waitpid()`](https://docs.python.org/3.14/library/os.html#os.waitpid) yields on the child process.

[Subject index](INDEX.md) · [Previous](pty-pseudo-terminal-utilities.md) · [Continue](example.md)
