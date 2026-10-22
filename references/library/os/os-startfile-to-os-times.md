# os: `os.startfile()`, `os.system()`, `os.times()`

os.startfile(*path*[, *operation*][, *arguments*][, *cwd*][, *show_cmd*])

Open a file with whatever application is associated with it.

With *operation* left unspecified, the effect is like double-clicking the file in Windows Explorer, or handing the file name as an argument to the **start** command at the interactive command shell: the file opens in whichever application (if any) its extension is tied to.

When some other *operation* is supplied, it must be a "command verb" describing what to do with the file. The common verbs Microsoft documents are `'open'`, `'print'` and `'edit'` (applied to files) plus `'explore'` and `'find'` (applied to directories).

While launching an application, hand *arguments* over as one single string. This argument might have no bearing when the function is used to launch a document.

By default the working directory is inherited, though the *cwd* argument can override it. That should be an absolute path. A relative *path* gets resolved against this argument.

Apply *show_cmd* to override the default window style. Whether that makes any difference rides on which application is being launched. The values are integers, as the Win32 `ShellExecute()` function supports.

`startfile()` returns the instant the associated application starts up. There is no option to wait for the application to close, nor any way to retrieve the application's exit status. The *path* parameter is taken relative to the current directory or *cwd*. To use an absolute path, be sure the first character is not a slash (`'/'`) Use [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) or the [`os.path.normpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.normpath) function so that paths come out properly encoded for Win32.

So that interpreter startup stays lean, the Win32 `ShellExecute()` function is not resolved until this function first runs. If the function cannot be resolved, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) will be raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.startfile` with arguments `path`, `operation`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.startfile/2` with arguments `path`, `operation`, `arguments`, `cwd`, `show_cmd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Changed in version 3.10: the *arguments*, *cwd* and *show_cmd* arguments were added, along with the `os.startfile/2` audit event.

 os.system(*command*)

Run the command (a string) within a subshell. The implementation calls the Standard C function `system()`, and inherits its limitations. Modifications to [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), and the like, do not show up in the executed command's environment. Any output the *command* produces is sent on to the interpreter standard output stream. Because the C standard leaves the meaning of the C function's return value undefined, the Python function's return value is likewise system-dependent.

Under Unix, the return value is the process exit status encoded in the format `wait()` specifies.

Under Windows, the return value is whatever the system shell returns once *command* runs. The Windows environment variable `COMSPEC` names the shell: typically **cmd.exe**, which returns the exit status of the command it ran; on systems running a non-native shell, check your shell documentation.

The [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module offers more capable facilities for spawning new processes and collecting their results; using that module is recommended over using this function. Look at the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3.14/library/subprocess.html#subprocess-replacements) section within the `subprocess` documentation for several handy recipes.

Under Unix, `waitstatus_to_exitcode()` can convert the result (the exit status) into an exit code. Under Windows, the result already is the exit code.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.system` with argument `command`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.

 os.times()

Give back the current global process times. The return value is an object carrying five attributes:

- `user` - user time

- `system` - system time

- `children_user` - user time of all child processes

- `children_system` - system time of all child processes

- `elapsed` - elapsed real time since a fixed point in the past

To keep backwards compatibility, this object also acts like a five-tuple holding `user`, `system`, `children_user`, `children_system`, and `elapsed` in that order.

Refer to the Unix manual page *[times(2)](https://manpages.debian.org/times(2))* and the [times(3)](https://man.freebsd.org/cgi/man.cgi?time(3)) manual page on Unix, or to [the GetProcessTimes MSDN](https://docs.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesstimes) on Windows. Under Windows, only `user` and `system` carry known values; the rest of the attributes are zero.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.3: the return type moved from a plain tuple to a tuple-like object that carries named attributes.

[Subject index](INDEX.md) · [Previous](os-spawnl-to-os-p-overlay.md) · [Continue](os-wait-to-os-waitid.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
