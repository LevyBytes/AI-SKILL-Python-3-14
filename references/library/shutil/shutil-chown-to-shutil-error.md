# shutil: `shutil.chown()`, `shutil.which()`, `shutil.Error`

shutil.chown(*path*, *user=None*, *group=None*, ***, *dir_fd=None*, *follow_symlinks=True*)

Alter the owner *user* and/or *group* of the supplied *path*.

The value *user* can be a system user name or a uid; the same goes for *group*. You must supply at least one argument.

See also [`os.chown()`](https://docs.python.org/3.14/library/os.html#os.chown), the underlying function.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.chown` with arguments `path`, `user`, `group`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

Changed in version 3.13: The *dir_fd* and *follow_symlinks* parameters were introduced.

 shutil.which(*cmd*, *mode=os.F_OK | os.X_OK*, *path=None*)

Return the path of an executable that would run if the supplied *cmd* were invoked. When no *cmd* would run, return `None`.

The value *mode* is a permission mask handed to [`os.access()`](https://docs.python.org/3.14/library/os.html#os.access), which by default checks whether the file exists and is executable.

The value *path* is a "`PATH` string" naming the directories to search, separated by [`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep). With no *path* given, the `PATH` environment variable is read out of [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ), falling back to [`os.defpath`](https://docs.python.org/3.14/library/os.html#os.defpath) when it is unset.

When *cmd* includes a directory component, `which()` checks only the given path directly and does not scan the directories listed in *path* or in the system's `PATH` environment variable.

Under Windows, the current directory is placed ahead of the *path* when *mode* leaves out `os.X_OK`. When *mode* does include `os.X_OK`, the Windows API `NeedCurrentDirectoryForExePathW` is consulted to decide whether the current directory should be placed ahead of *path*. So that the current working directory is not consulted for executables, set the environment variable `NoDefaultCurrentDirectoryInExePath`.

Also under Windows, the `PATHEXT` environment variable serves to resolve commands that might not already carry an extension. As an example, when you call `shutil.which("python")`, `which()` consults `PATHEXT` to learn that it ought to look for `python.exe` inside the *path* directories. For example, on Windows:

```python
>>> shutil.which("python")
'C:\\Python33\\python.EXE'

```

The same applies when *cmd* is a path holding a directory component:

```python
>>> shutil.which("C:\\Python33\\python")
'C:\\Python33\\python.EXE'

```

Added in version 3.3.

Changed in version 3.8: The [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type is now accepted. When *cmd* is of type `bytes`, the result is `bytes` as well.

Changed in version 3.12: Under Windows, the current directory is no longer placed ahead of the search path when *mode* includes `os.X_OK` and the WinAPI call `NeedCurrentDirectoryForExePathW(cmd)` returns false; otherwise the current directory is placed ahead even when it already appears in the search path. `PATHEXT` is now applied even when *cmd* carries a directory component or finishes with an extension that `PATHEXT` lists, and filenames lacking any extension can now be located.

 *exception *shutil.Error

Across a multi-file operation, this exception collects whatever exceptions get raised. In the `copytree()` case, the argument to the exception is a list whose entries are 3-tuples (*srcname*, *dstname*, *exception*).

[Subject index](INDEX.md) · [Previous](shutil-rmtree-to-shutil-disk-usage.md) · [Continue](platform-dependent-efficient-copy-operations.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md) · [Owning module, declaration or section: Directory and files operations](shutil-copyfileobj-to-shutil-copystat.md)
