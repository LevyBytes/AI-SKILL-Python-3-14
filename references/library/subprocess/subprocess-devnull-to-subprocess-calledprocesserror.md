# subprocess: `subprocess.DEVNULL`, `subprocess.PIPE`, `subprocess.STDOUT`, `subprocess.SubprocessError`, `subprocess.TimeoutExpired`, `subprocess.CalledProcessError`

subprocess.DEVNULL

A special value you can hand to `Popen` as the *stdin*, *stdout* or *stderr* argument; it signals that the special file [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) is to be used.

Added in version 3.3.

 subprocess.PIPE

A special value you can hand to `Popen` as the *stdin*, *stdout* or *stderr* argument; it signals that a pipe to the standard stream ought to be opened. It is most handy together with `Popen.communicate()`.

 subprocess.STDOUT

A special value you can hand to `Popen` as the *stderr* argument; it signals that standard error ought to be sent into the very same handle as standard output.

 *exception *subprocess.SubprocessError

The base class underlying every other exception raised by this module.

Added in version 3.3.

 *exception *subprocess.TimeoutExpired

A subclass of `SubprocessError` that is raised once a timeout runs out while a child process is being waited on.

 cmd

The command that spawned the child process.

 timeout

Timeout in seconds.

 output

The output of the child process when it was captured by `run()` or `check_output()`. If it wasn't, then `None`. Whenever any output got captured, this is always [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), no matter what the `text=True` setting was. When no output appeared, it can stay `None` rather than `b''`.

 stdout

An alias for output, kept for symmetry with `stderr`.

 stderr

The stderr output of the child process when it was captured by `run()`. If it wasn't, then `None`. Whenever stderr output got captured, this is always [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), no matter what the `text=True` setting was. When no stderr output appeared, it can stay `None` rather than `b''`.

Added in version 3.3.

Changed in version 3.5: *stdout* and *stderr* attributes added

 *exception *subprocess.CalledProcessError

A subclass of `SubprocessError` that is raised once a process started by `check_call()`, `check_output()`, or `run()` (with `check=True`) comes back with a non-zero exit status.

 returncode

The exit status of the child process. Should the process have exited because of a signal, this holds the negative signal number.

 cmd

The command that spawned the child process.

 output

The output of the child process when it was captured by `run()` or `check_output()`. If it wasn't, then `None`.

 stdout

An alias for output, kept for symmetry with `stderr`.

 stderr

The stderr output of the child process when it was captured by `run()`. If it wasn't, then `None`.

Changed in version 3.5: *stdout* and *stderr* attributes added

[Subject index](INDEX.md) · [Previous](completed-process-result-and-return-code.md) · [Continue](frequently-used-arguments.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: Using the `subprocess` Module](subprocess-run.md)
