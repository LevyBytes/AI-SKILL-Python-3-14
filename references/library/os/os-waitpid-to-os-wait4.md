# os.waitid: Wait-result process fields and child resource usage

*idtype* may be `P_PID`, `P_PGID`, `P_ALL`, or (under Linux) `P_PIDFD`. How *id* gets read hinges on which one you pick; consult each of their separate descriptions.

*options* combines flags with OR. You must supply at least one of `WEXITED`, `WSTOPPED` or `WCONTINUED`; `WNOHANG` and `WNOWAIT` serve as extra optional flags.

What comes back is an object that mirrors the data held in the `siginfo_t` structure, carrying these attributes:

- `si_pid` (process ID)

- `si_uid` (real user ID of the child)

- `si_signo` (always [`SIGCHLD`](https://docs.python.org/3.14/library/signal.html#signal.SIGCHLD))

- `si_status` (the exit status or signal number, depending on `si_code`)

- `si_code` (see `CLD_EXITED` for possible values)

Should `WNOHANG` be supplied while no matching children sit in the requested state, `None` comes back. Failing that, when no matching children remain that could be waited for, [`ChildProcessError`](https://docs.python.org/3.14/library/exceptions.html#ChildProcessError) is raised.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

Added in version 3.3.

Changed in version 3.13: This function now works on macOS too.

 os.waitpid(*pid*, *options*, */*)

How this function behaves is not the same on Unix and Windows.

On Unix: Block until the child process named by process id *pid* completes, then return a tuple holding its process id together with an exit status indication (encoded the way `wait()` encodes it). The integer *options* value shapes the semantics of the call, and should be `0` for ordinary operation.

When *pid* exceeds `0`, `waitpid()` asks for status information about that one specific process. When *pid* is `0`, the request covers the status of any child belonging to the process group of the current process. When *pid* is `-1`, the request reaches any child of the current process. When *pid* falls below `-1`, status is sought for any process within the process group `-pid` (the absolute value of *pid*).

*options* combines flags with OR. Where it carries `WNOHANG` and no matching children sit in the requested state, `(0, 0)` comes back. Failing that, when no matching children remain that could be waited for, [`ChildProcessError`](https://docs.python.org/3.14/library/exceptions.html#ChildProcessError) is raised. Among the other usable options are `WUNTRACED` and `WCONTINUED`.

On Windows: Block until the process named by process handle *pid* completes, then return a tuple holding *pid* plus its exit status shifted left by 8 bits (that shift makes the function easier to use across platforms). On Windows a *pid* at or below `0` carries no special meaning and triggers an exception. The integer *options* value has no bearing here. *pid* may name any process whose id is known, not strictly a child process. The `spawn*` functions invoked with `P_NOWAIT` hand back suitable process handles.

`waitstatus_to_exitcode()` can be used to convert the exit status into an exit code.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.

Changed in version 3.5: When the system call gets interrupted and the signal handler raises no exception, the function now retries the system call rather than raising an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 os.wait3(*options*)

Behaves like `waitpid()`, save that no process id argument is supplied and a 3-element tuple holding the child's process id, exit status indication, and resource usage information comes back. Turn to [`resource.getrusage()`](https://docs.python.org/3.14/library/resource.html#resource.getrusage) for the particulars of resource usage information. The *options* argument matches the one handed to `waitpid()` and `wait4()`.

`waitstatus_to_exitcode()` can be used to convert the exit status into an exitcode.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.wait4(*pid*, *options*)

Behaves like `waitpid()`, save that a 3-element tuple, holding the child's process id, exit status indication, and resource usage information comes back. Turn to [`resource.getrusage()`](https://docs.python.org/3.14/library/resource.html#resource.getrusage) for the particulars of resource usage information. The arguments of `wait4()` match those handed to `waitpid()`.

`waitstatus_to_exitcode()` can be used to convert the exit status into an exitcode.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

[Subject index](INDEX.md) · [Continue](os-p-pid-to-os-wnowait.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md) · [Owning module, declaration or section: os.waitid](os-wait-to-os-waitid.md) · [Preceding source contract and version conditions](os-wait-to-os-waitid.md)
