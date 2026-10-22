# os: `os.posix_spawnp()`, `os.register_at_fork()`

os.posix_spawnp(*path*, *argv*, *env*, ***, *file_actions=None*, *setpgroup=None*, *resetids=False*, *setsid=False*, *setsigmask=()*, *setsigdef=()*, *scheduler=None*)

Wraps the `posix_spawnp()` C library API for use from Python.

Behaves like `posix_spawn()`, except the system hunts for the *executable* file across the directories listed in the `PATH` environment variable (the same fashion that `execvp(3)` uses).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.posix_spawn` with arguments `path`, `argv`, `env`.

Added in version 3.8.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX, not WASI, not Android, not iOS.

See `posix_spawn()` documentation.

 os.register_at_fork(***, *before=None*, *after_in_parent=None*, *after_in_child=None*)

Register callables to run whenever a new child process is forked by way of `os.fork()` or comparable process-cloning APIs. The parameters are all optional and keyword-only. Each one names a distinct call point.

- *before* is a function invoked ahead of forking a child process.

- *after_in_parent* is a function invoked within the parent process once a child process has been forked.

- *after_in_child* is a function invoked within the child process.

These calls happen only when control is expected to come back to the Python interpreter. A standard [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) launch will not fire them, because the child never re-enters the interpreter.

Functions registered to run before forking fire in reverse registration order. Functions registered to run after forking (whether in the parent or in the child) fire in registration order.

Keep in mind that `fork()` calls issued by third-party C code may skip those functions entirely, unless that code explicitly calls [`PyOS_BeforeFork()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_BeforeFork), [`PyOS_AfterFork_Parent()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Parent) and [`PyOS_AfterFork_Child()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Child).

A registered function cannot be unregistered.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](os-popen-to-os-posix-spawn-closefrom.md) · [Continue](os-spawnl-to-os-p-overlay.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
