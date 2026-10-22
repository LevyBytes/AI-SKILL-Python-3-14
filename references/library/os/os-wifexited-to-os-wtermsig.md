# os: `os.WIFEXITED()`, `os.WEXITSTATUS()`, `os.WSTOPSIG()`, `os.WTERMSIG()`

os.WIFEXITED(*status*)

Return `True` when the process exited normally, meaning by calling `exit()` or `_exit()`, or by returning from `main()`; otherwise return `False`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WEXITSTATUS(*status*)

Return the process exit status.

Only employ this function when `WIFEXITED()` is true.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WSTOPSIG(*status*)

Return the signal that brought the process to a stop.

Only employ this function when `WIFSTOPPED()` is true.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

 os.WTERMSIG(*status*)

Return the number of the signal that terminated the process.

Only employ this function when `WIFSIGNALED()` is true.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

[Subject index](INDEX.md) · [Previous](os-cld-exited-to-os-wifsignaled.md) · [Continue](os-sched-other-to-os-sched-reset-on-fork.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
