# os: Child-process status codes and wait-result interpretation

os.CLD_EXITED

 os.CLD_KILLED

 os.CLD_DUMPED

 os.CLD_TRAPPED

 os.CLD_STOPPED

 os.CLD_CONTINUED

These make up the possible values for `si_code` in the result that `waitid()` returns.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

Added in version 3.3.

Changed in version 3.9: Added `CLD_KILLED` and `CLD_STOPPED` values.

 os.waitstatus_to_exitcode(*status*)

Turn a wait status into an exit code.

On Unix:

- When the process exited normally (when `WIFEXITED(status)` is true), return the process exit status (return `WEXITSTATUS(status)`): a result at or above 0.

- When a signal terminated the process (when `WIFSIGNALED(status)` is true), return `-signum`, where *signum* is the number of the signal that brought the process down (return `-WTERMSIG(status)`): a result below 0.

- Failing those, raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

On Windows, return *status* shifted right by 8 bits.

On Unix, when the process is being traced or when `waitpid()` was invoked with the `WUNTRACED` option, the caller has to first check whether `WIFSTOPPED(status)` is true. Do not call this function while `WIFSTOPPED(status)` is true.

See also

`WIFEXITED()`, `WEXITSTATUS()`, `WIFSIGNALED()`, `WTERMSIG()`, `WIFSTOPPED()`, `WSTOPSIG()` functions.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.

Added in version 3.9.

The functions that follow accept a process status code as returned by `system()`, `wait()`, or `waitpid()` as a parameter. They serve to work out the disposition of a process.

 os.WCOREDUMP(*status*, */*)

Return `True` when a core dump was generated for the process, otherwise return `False`.

Only employ this function when `WIFSIGNALED()` is true.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WIFCONTINUED(*status*)

Return `True` when a stopped child has resumed through delivery of [`SIGCONT`](https://docs.python.org/3.14/library/signal.html#signal.SIGCONT) (when the process has continued from a job control stop), otherwise return `False`.

See the `WCONTINUED` option.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WIFSTOPPED(*status*)

Return `True` when a delivered signal stopped the process, otherwise return `False`.

`WIFSTOPPED()` returns `True` solely when the `waitpid()` call used the `WUNTRACED` option or while the process is being traced (see *[ptrace(2)](https://manpages.debian.org/ptrace(2))*).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WIFSIGNALED(*status*)

Return `True` when a signal terminated the process, otherwise return `False`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

[Subject index](INDEX.md) · [Previous](os-p-pid-to-os-wnowait.md) · [Continue](os-wifexited-to-os-wtermsig.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
