# subprocess - Popen Constructor - Contract: Changed in version 3.8: On Windows, the *executable* parameter takes both bytes and a path-like object.

Changed in version 3.8: On Windows, the *executable* parameter takes both bytes and a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.12: On Windows the lookup order for the shell under `shell=True` was revised. In place of the current directory and `%PATH%`, it now uses `%COMSPEC%` together with `%SystemRoot%\System32\cmd.exe`. Consequently, planting a hostile binary called `cmd.exe` in a current directory is no longer effective.

*stdin*, *stdout* and *stderr* designate the standard input, standard output and standard error file handles, respectively, for the program being run. Acceptable values are `None`, `PIPE`, `DEVNULL`, an existing file descriptor (a positive integer), and an existing [file object](https://docs.python.org/3.14/glossary.html#term-file-object) holding a valid file descriptor. Under the default of `None`, nothing is redirected. `PIPE` means a fresh pipe to the child is to be created. `DEVNULL` means the special file [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) is to be used. On top of that, *stderr* may be `STDOUT`, which routes the applications' stderr stream into whichever file handle already serves *stdout*.

When *preexec_fn* is set to a callable object, that object gets invoked inside the child process right before the child is run. (POSIX only)

Warning

Using the *preexec_fn* parameter is NOT SAFE whenever your application has threads running. Before exec gets called, the child process may deadlock.

Note

When you have to adjust the environment for the child, use the *env* parameter rather than handling it inside a *preexec_fn*. The *start_new_session* and *process_group* parameters ought to replace code that used *preexec_fn* to call [`os.setsid()`](https://docs.python.org/3.14/library/os.html#os.setsid) or [`os.setpgid()`](https://docs.python.org/3.14/library/os.html#os.setpgid) inside the child.

Changed in version 3.8: Subinterpreters no longer support the *preexec_fn* parameter. Calling it from within a subinterpreter raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). Applications running under mod_wsgi, uWSGI, and similar embedded environments may feel the impact of this fresh restriction.

When *close_fds* is true, every file descriptor other than `0`, `1` and `2` is closed before the child process runs. On the other hand, when *close_fds* is false, file descriptors follow their inheritable flag as laid out in [Inheritance of File Descriptors](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Under Windows, when *close_fds* is true the child process inherits no handles unless they are passed in explicitly via the `handle_list` element of `STARTUPINFO.lpAttributeList`, or by standard handle redirection.

Changed in version 3.2: For *close_fds*, the default shifted away from [`False`](https://docs.python.org/3.14/library/constants.html#False) to the behavior outlined above.

Changed in version 3.7: When the standard handles are being redirected on Windows, the default for *close_fds* moved from [`False`](https://docs.python.org/3.14/library/constants.html#False) over to [`True`](https://docs.python.org/3.14/library/constants.html#True). You can now also set *close_fds* to `True` even while redirecting those standard handles.

*pass_fds* is an optional sequence of file descriptors meant to stay open across the parent and the child. Supplying any *pass_fds* at all compels *close_fds* to become [`True`](https://docs.python.org/3.14/library/constants.html#True). (POSIX only)

Changed in version 3.2: The *pass_fds* parameter was added.

When *cwd* is not `None`, the function switches the working directory to *cwd* before it runs the child. *cwd* may be a string, bytes or [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) object. Under POSIX, when the executable path is a relative path, the function searches for *executable* (or for the first item in *args*) relative to *cwd*.

[Subject index](INDEX.md) · [Previous](subprocess-popen-class.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: subprocess.Popen](subprocess-popen-class.md) · [Owning module, declaration or section: Popen Constructor](popen-constructor.md) · [Required continuation of the source contract](popen-working-directory-and-platform-options.md)
