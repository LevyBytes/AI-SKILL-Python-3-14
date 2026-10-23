# os`os` - Miscellaneous operating system interfaces

### `os` - Miscellaneous operating system interfaces

**Source code:** [Lib/os.py](https://github.com/python/cpython/tree/3.14/Lib/os.py)

---

This module gives you a portable means of tapping operating-system-dependent functionality. When all you need is to read from or write to a file, look at [`open()`](https://docs.python.org/3.14/library/functions.html#open); when you need to manipulate paths, look at the [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) module; and when you need to read every line across every file named on the command line, look at the [`fileinput`](https://docs.python.org/3.14/library/fileinput.html#module-fileinput) module. To create temporary files and directories, look at the [`tempfile`](https://docs.python.org/3.14/library/tempfile.html#module-tempfile) module, and for high-level file and directory handling, look at the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module.

A few notes about where these functions are available:

- Every built-in operating-system-dependent module of Python is designed so that, wherever the same functionality exists, the same interface is used; for instance, the function `os.stat(path)` hands back stat information about *path* in one consistent format (which, as it happens, came out of the POSIX interface).

- Extensions specific to one particular operating system are reachable through the `os` module too, though leaning on them naturally puts portability at risk.

- Every function that accepts path or file names takes both bytes and string objects, and produces an object of that same type whenever a path or file name is returned.

- Under VxWorks, os.popen, os.fork, os.execv and os.spawn*p* are unsupported.

- Under WebAssembly platforms, Android and iOS, sizable portions of the `os` module are missing or act differently. The APIs tied to processes (such as `fork()`, `execve()`) and to resources (such as `nice()`) are missing. Others, like `getuid()` and `getpid()`, are emulated or stubbed. WebAssembly platforms also have no signal support (such as `kill()`, `wait()`).

Note

For invalid or inaccessible file names and paths, or for other arguments that have the right type yet are rejected by the operating system, every function within this module raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) (or one of its subclasses).

 *exception *os.error

An alias for the built-in [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception.

 os.name

The name of the operating-system-dependent module that got imported. So far the names registered are: `'posix'`, `'nt'`, `'java'`.

See also

[`sys.platform`](https://docs.python.org/3.14/library/sys.html#sys.platform) offers finer granularity. `os.uname()` supplies system-dependent version information.

The [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform) module supplies detailed checks of the system's identity.

[Subject index](INDEX.md) · [Continue](file-names-command-line-arguments-and-environment-variables.md)
