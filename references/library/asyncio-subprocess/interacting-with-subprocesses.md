# asyncio.subprocess: Async subprocess PID and return-code fields

pid

Process identification number (PID).

Keep in mind that for processes spawned by the `create_subprocess_shell()` function, this attribute holds the PID of the shell that was launched.

 returncode

Return code of the process when it exits.

When the value is `None`, that signals the process has yet to terminate.

For processes spawned with `create_subprocess_exec()`, a negative value `-N` signals that the child was terminated by signal `N` (POSIX only).

For processes spawned with `create_subprocess_shell()`, the return code mirrors the exit status of the shell itself (for instance `/bin/sh`), which can translate signals into codes such as `128+N`. Consult the shell's own documentation (the Bash manual's Exit Status, say) for the specifics.

[Subject index](INDEX.md) · [Previous](subprocess-wait-communicate-and-signals.md) · [Continue](subprocess-and-threads.md) · [Owning module, declaration or section: asyncio.subprocess.Process](asyncio-subprocess-process-class.md) · [Owning module, declaration or section: Interacting with Subprocesses](asyncio-subprocess-process-class.md)
