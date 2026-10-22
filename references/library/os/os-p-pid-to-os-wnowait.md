# os: `os.P_PID`, `os.P_PGID`, `os.P_ALL`, `os.P_PIDFD`, `os.WCONTINUED`, `os.WEXITED`, `os.WSTOPPED`, `os.WUNTRACED`, `os.WNOHANG`, `os.WNOWAIT`

os.P_PID

 os.P_PGID

 os.P_ALL

 os.P_PIDFD

These make up the possible values for *idtype* within `waitid()`. They govern how *id* is read:

- `P_PID` - wait for the child whose PID is *id*.

- `P_PGID` - wait for any child whose progress group ID is *id*.

- `P_ALL` - wait for any child; *id* is ignored.

- `P_PIDFD` - wait for whichever child the file descriptor *id* identifies (a process file descriptor that `pidfd_open()` made).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

Note

`P_PIDFD` is only available on Linux >= 5.4.

Added in version 3.3.

Added in version 3.9: The `P_PIDFD` constant.

 os.WCONTINUED

When set as an *options* flag for `waitpid()`, `wait3()`, `wait4()`, and `waitid()`, this reports child processes that have resumed from a job control stop since the last time they were reported.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WEXITED

When set as an *options* flag for `waitid()`, this reports child processes that have terminated.

The remaining `wait*` functions always report children that have terminated, so the option is absent for them.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

Added in version 3.3.

 os.WSTOPPED

When set as an *options* flag for `waitid()`, this reports child processes that a delivered signal has stopped.

The other `wait*` functions do not offer this option.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

Added in version 3.3.

 os.WUNTRACED

When set as an *options* flag for `waitpid()`, `wait3()`, and `wait4()`, this additionally reports child processes that have been stopped while their current state has gone unreported since they were stopped.

`waitid()` does not offer this option.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WNOHANG

As an *options* flag, this makes `waitpid()`, `wait3()`, `wait4()`, and `waitid()` come back immediately when no child process status is available at once.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WNOWAIT

As an *options* flag, this makes `waitid()` keep the child in a waitable state, so a later `wait*()` call can fetch the child status information once more.

The other `wait*` functions do not offer this option.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

[Subject index](INDEX.md) · [Previous](os-waitpid-to-os-wait4.md) · [Continue](os-cld-exited-to-os-wifsignaled.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
