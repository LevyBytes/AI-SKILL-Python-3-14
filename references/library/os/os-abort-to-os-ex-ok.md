# os: `os.abort()`, `os.add_dll_directory()`, `os.execl()`, `os.execle()`, `os.execlp()`, `os.execlpe()`, `os.execv()`, `os.execve()`, `os.execvp()`, `os.execvpe()`, `os._exit()`, `os.EX_OK`

### Process Management

These functions may serve to create and manage processes.

Each of the `exec*` functions takes a list of arguments meant for the new program loaded into the process. Every time, that first argument reaches the new program as the program's own name, not as something a user would have entered at a command line. To a C programmer, this is the `argv[0]` passed into a program's `main()`. As an illustration, `os.execv('/bin/echo', ['foo', 'bar'])` prints just `bar` on standard output; `foo` seems to get dropped.

 os.abort()

Raise a `SIGABRT` signal against the current process. On Unix, a core dump is the default outcome; on Windows, the process returns an exit code of `3` right away. Keep in mind that calling this function does not trigger the Python signal handler that was registered for `SIGABRT` via [`signal.signal()`](https://docs.python.org/3.14/library/signal.html#signal.signal).

 os.add_dll_directory(*path*)

Add a path to the DLL search path.

This search path is consulted while dependencies get resolved for imported extension modules (the module itself goes through [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) instead), and [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) consults it as well.

To remove the directory, call **close()** on the object that was returned, or place that object inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

Consult the [Microsoft documentation](https://msdn.microsoft.com/44228cf2-6306-466c-8f16-f513cd3ba8b5) for more information about how DLLs get loaded.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.add_dll_directory` with argument `path`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.8: CPython releases before this one would resolve DLLs through the default behavior tied to the current process. That produced inconsistencies, among them only occasionally searching `PATH` or the current working directory, and OS functions like `AddDllDirectory` taking no effect.

As of 3.8, the two main routes by which DLLs get loaded now explicitly override the process-wide behavior so consistency is guaranteed. Consult the [porting notes](https://docs.python.org/3.14/whatsnew/3.8.html#bpo-36085-whatsnew) for information on updating libraries.

 os.execl(*path*, *arg0*, *arg1*, *...*)

 os.execle(*path*, *arg0*, *arg1*, *...*, *env*)

 os.execlp(*file*, *arg0*, *arg1*, *...*)

 os.execlpe(*file*, *arg0*, *arg1*, *...*, *env*)

 os.execv(*path*, *args*)

 os.execve(*path*, *args*, *env*)

 os.execvp(*file*, *args*)

 os.execvpe(*file*, *args*, *env*)

Every one of these functions runs a new program in place of the current process; none of them return. On Unix, the new executable loads into the current process and will keep the same process id the caller had. Errors come back as [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exceptions.

Replacement of the current process happens immediately. Open file objects and descriptors do not get flushed, so when data may be buffered on these open files, flush them with [`flush()`](https://docs.python.org/3.14/library/io.html#io.IOBase.flush) or `os.fsync()` before you call an `exec*` function.

Where the "l" and "v" variants of the `exec*` functions part ways is in how command-line arguments reach the function. The "l" variants tend to be the simplest to use when the parameter count is fixed as the code is written; each parameter just turns into an extra parameter to the `execl*()` functions. The "v" variants fit well when the parameter count varies, the arguments handed over in a list or tuple as the *args* parameter. In either situation, the child process arguments should start with the name of the command being run, though nothing enforces that.

Those variants bearing a "p" near the end (`execlp()`, `execlpe()`, `execvp()`, and `execvpe()`) draw on the `PATH` environment variable to locate the program *file*. While the environment is being replaced (through one of the `exec*e` variants, treated in the next paragraph), the new environment supplies the `PATH` variable. The remaining variants, `execl()`, `execle()`, `execv()`, and `execve()`, do not draw on the `PATH` variable to locate the executable; *path* has to hold a suitable absolute or relative path. A relative path has to include at least one slash, even on Windows, because plain names get no resolution.

For `execle()`, `execlpe()`, `execve()`, and `execvpe()` (note that each of these ends in "e"), the *env* parameter has to be a mapping used to set the environment variables for the new process (these stand in for the current process' environment); the functions `execl()`, `execlp()`, `execv()`, and `execvp()` instead make the new process inherit the environment that the current process has.

For `execve()` on certain platforms, *path* may additionally be given as an open file descriptor. Your platform might not support this functionality; you can confirm its presence by checking `os.supports_fd`. Where it is missing, using it raises a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.exec` with arguments `path`, `args`, `env`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.

Changed in version 3.3: Giving *path* as an open file descriptor for `execve()` is now supported.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os._exit(*n*)

Exit the process with status *n*, skipping cleanup handlers, the flushing of stdio buffers, and so on.

Note

The usual route for exiting is [`sys.exit(n)`](https://docs.python.org/3.14/library/sys.html#sys.exit). As a rule, reserve `_exit()` for the child process following a `fork()`.

The exit codes below are defined and can be passed to `_exit()`, though using them is not required. They generally suit system programs written in Python, for example the external command delivery program of a mail server.

Note

A few of these may be absent on certain Unix platforms, given some variation across them. Each constant is defined wherever the underlying platform defines it.

 os.EX_OK

Exit code that means no error occurred. May be drawn from the defined value of `EXIT_SUCCESS` on some platforms. Generally carries a value of zero.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

[Subject index](INDEX.md) · [Previous](os-getxattr-to-os-xattr-replace.md) · [Continue](os-ex-usage-to-os-ex-noperm.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
