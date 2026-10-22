# os: `os.wait()`, `os.waitid()`

os.wait()

Block until a child process completes, then return a tuple holding its pid alongside an exit-status indication. That indication is a 16-bit number: its low byte carries the signal number responsible for killing the process, while its high byte carries the exit status (in the case where the signal number is zero); the high bit within the low byte gets set whenever a core file was produced.

When no children remain that could be waited for, [`ChildProcessError`](https://docs.python.org/3.14/library/exceptions.html#ChildProcessError) is raised.

`waitstatus_to_exitcode()` can convert the exit status into an exit code.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

See also

The remaining `wait*()` functions documented below let you wait for a particular child process to complete and offer more options. `waitpid()` is the sole one available on Windows as well.

 os.waitid(*idtype*, *id*, *options*, */*)

Block until a child process completes.

[Subject index](INDEX.md) · [Previous](os-startfile-to-os-times.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md) · [Required continuation of the source contract](os-waitpid-to-os-wait4.md)
