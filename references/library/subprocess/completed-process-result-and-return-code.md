# subprocess: `subprocess.CompletedProcess`, `check_returncode()`

*class *subprocess.CompletedProcess

What `run()` hands back, standing for a process that has run to completion.

 args

The arguments that were used to start the process. It can be either a list or a string.

 returncode

The exit status of the child process. As a rule, an exit status of 0 signals that it succeeded.

When the value is a negative `-N`, it tells you the child was ended by signal `N` (POSIX only).

 stdout

The captured stdout coming from the child process. It is a bytes sequence, or a string when `run()` was invoked with an encoding, errors, or text=True. It is `None` when stdout went uncaptured.

When you have run the process with `stderr=subprocess.STDOUT`, stdout and stderr land merged together in this attribute, and `stderr` ends up being `None`.

 stderr

The captured stderr coming from the child process. It is a bytes sequence, or a string when `run()` was invoked with an encoding, errors, or text=True. It is `None` when stderr went uncaptured.

 check_returncode()

When `returncode` is non-zero, raise a `CalledProcessError`.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](subprocess-run.md) · [Continue](subprocess-devnull-to-subprocess-calledprocesserror.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: Using the `subprocess` Module](subprocess-run.md)
