# os: `os.popen()`, `os.posix_spawn()`, `os.POSIX_SPAWN_OPEN`, `os.POSIX_SPAWN_CLOSE`, `os.POSIX_SPAWN_DUP2`, `os.POSIX_SPAWN_CLOSEFROM`

os.popen(*cmd*, *mode='r'*, *buffering=-1*)

Open a pipe leading to or from the command *cmd*. What comes back is an open file object joined to the pipe; whether you read from it or write to it follows from *mode* being `'r'` (default) or `'w'`. The *buffering* argument carries the same meaning as the matching argument of the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function. That returned file object handles text strings rather than bytes.

When the subprocess finishes cleanly, the `close` method gives back [`None`](https://docs.python.org/3.14/library/constants.html#None); if a problem occurred, it gives the subprocess's return code. Under POSIX, a positive return code stands for the process's return value left-shifted by one byte. A negative return code means the process died from the signal whose number is the negated return code. (As an illustration, the return value could be `- signal.SIGKILL` when the subprocess was killed.) Under Windows, the return value carries the signed integer return code coming from the child process.

Under Unix, you can apply `waitstatus_to_exitcode()` to turn the `close` method's result (the exit status) into an exit code whenever it is not `None`. Under Windows, the `close` method's result already is the exit code (or `None`).

The implementation rests on [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen); refer to that class's documentation for richer ways to manage and talk to subprocesses.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI, not Android, not iOS.

Note

The Python UTF-8 Mode influences which encodings apply to *cmd* and to the pipe contents.

`popen()` is just a thin wrapper over [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen). Turn to `subprocess.Popen` or [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) when you need control over options such as encodings.

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.14: The [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module is recommended instead.

 os.posix_spawn(*path*, *argv*, *env*, ***, *file_actions=None*, *setpgroup=None*, *resetids=False*, *setsid=False*, *setsigmask=()*, *setsigdef=()*, *scheduler=None*)

Wraps the `posix_spawn()` C library API for use from Python.

For most needs, prefer [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) over `posix_spawn()`.

The positional-only arguments *path*, *args*, and *env* mirror those of `execve()`. You may pass `None` for *env*, and then the current process' environment applies.

The *path* parameter gives the path leading to the executable file. That *path* ought to include a directory. To supply an executable file lacking a directory, use `posix_spawnp()`.

The *file_actions* argument can be a sequence of tuples that spell out actions performed on particular file descriptors inside the child process, occurring between the C library implementation's `fork()` and `exec()` steps. Each tuple's first item has to be one of the three type indicators listed below, which govern the remaining tuple elements:

 os.POSIX_SPAWN_OPEN

(`os.POSIX_SPAWN_OPEN`, *fd*, *path*, *flags*, *mode*)

Performs `os.dup2(os.open(path, flags, mode), fd)`.

 os.POSIX_SPAWN_CLOSE

(`os.POSIX_SPAWN_CLOSE`, *fd*)

Performs `os.close(fd)`.

 os.POSIX_SPAWN_DUP2

(`os.POSIX_SPAWN_DUP2`, *fd*, *new_fd*)

Performs `os.dup2(fd, new_fd)`.

 os.POSIX_SPAWN_CLOSEFROM

(`os.POSIX_SPAWN_CLOSEFROM`, *fd*)

Performs `os.closerange(fd, INF)`.

Those tuples map onto the C library `posix_spawn_file_actions_addopen()`, `posix_spawn_file_actions_addclose()`, `posix_spawn_file_actions_adddup2()`, and `posix_spawn_file_actions_addclosefrom_np()` API calls that set things up ahead of the `posix_spawn()` call itself.

The *setpgroup* argument sets the child's process group to whatever value you specify. Specifying 0 makes the child's process group ID equal to its process ID. Leaving *setpgroup* unset means the child inherits the parent's process group ID. This argument lines up with the C library `POSIX_SPAWN_SETPGROUP` flag.

When the *resetids* argument is `True`, it resets the child's effective UID and GID back to the parent process's real UID and GID. When the argument is `False`, the child keeps the parent's effective UID and GID. In both cases, should the executable file carry enabled set-user-ID and set-group-ID permission bits, the result of those bits overrides whatever the effective UID and GID would otherwise be. This argument lines up with the C library `POSIX_SPAWN_RESETIDS` flag.

When the *setsid* argument is `True`, it makes a new session ID for `posix_spawn`. *setsid* needs the `POSIX_SPAWN_SETSID` or `POSIX_SPAWN_SETSID_NP` flag. Without it, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) is raised.

The *setsigmask* argument sets the signal mask to whichever signal set you specify. Skip the parameter and the child inherits the parent's signal mask. This argument lines up with the C library `POSIX_SPAWN_SETSIGMASK` flag.

The *sigdef* argument resets the disposition of every signal in the specified set. This argument lines up with the C library `POSIX_SPAWN_SETSIGDEF` flag.

The *scheduler* argument has to be a tuple holding the (optional) scheduler policy plus an instance of `sched_param` carrying the scheduler parameters. Putting `None` where the scheduler policy goes signals that no policy is supplied. This argument blends the C library `POSIX_SPAWN_SETSCHEDPARAM` and `POSIX_SPAWN_SETSCHEDULER` flags.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.posix_spawn` with arguments `path`, `argv`, `env`.

Added in version 3.8.

Changed in version 3.13: the *env* parameter now accepts `None`. On platforms providing `posix_spawn_file_actions_addclosefrom_np()`, `os.POSIX_SPAWN_CLOSEFROM` becomes available.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

[Subject index](INDEX.md) · [Previous](os-kill-to-os-plock.md) · [Continue](os-posix-spawnp-to-os-register-at-fork.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
