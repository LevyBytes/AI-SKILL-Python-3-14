# subprocess: `Popen.stdout`, `Popen.stderr`, `Popen.pid`, `Popen.returncode`

Popen.stdout

When the *stdout* argument was `PIPE`, this attribute holds a readable stream object such as [`open()`](https://docs.python.org/3.14/library/functions.html#open) yields. Reading the stream delivers output from the child process. The stream is a text stream when the *encoding* or *errors* arguments were given, or when the *text* or *universal_newlines* argument was `True`; otherwise it is a byte stream. When the *stdout* argument was something other than `PIPE`, this attribute is `None`.

 Popen.stderr

When the *stderr* argument was `PIPE`, this attribute holds a readable stream object such as [`open()`](https://docs.python.org/3.14/library/functions.html#open) yields. Reading the stream delivers error output from the child process. The stream is a text stream when the *encoding* or *errors* arguments were given, or when the *text* or *universal_newlines* argument was `True`; otherwise it is a byte stream. When the *stderr* argument was something other than `PIPE`, this attribute is `None`.

Warning

Favor `communicate()` over `.stdin.write`, `.stdout.read` or `.stderr.read`, which sidesteps deadlocks that occur when one of the remaining OS pipe buffers fills and stalls the child process.

 Popen.pid

The child process's process ID.

Keep in mind that setting the *shell* argument to `True` makes this the process ID belonging to the shell that was spawned.

 Popen.returncode

The child return code. Starting out as `None`, `returncode` becomes set whenever a call to the `poll()`, `wait()`, or `communicate()` methods notices that the process has finished.

A value of `None` means the process had not yet finished as of the most recent method call.

A negative value `-N` signals that the child was terminated by signal `N` (POSIX only).

With `shell=True`, the return code mirrors the exit status of the shell itself (for example `/bin/sh`), which may translate signals into codes like `128+N`. Consult the shell's documentation (for instance, the Bash manual's Exit Status) for the particulars.

[Subject index](INDEX.md) · [Previous](popen-poll-to-popen-stdin.md) · [Continue](subprocess-startupinfo-class.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: Popen Objects](popen-poll-to-popen-stdin.md)
