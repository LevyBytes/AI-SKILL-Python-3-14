# os: `os.getenv()`, `os.getenvb()`, `os.get_exec_path()`, `os.getegid()`, `os.geteuid()`, `os.getgid()`, `os.getgrouplist()`, `os.getgroups()`, `os.getlogin()`, `os.getpgid()`, `os.getpgrp()`

os.getenv(*key*, *default=None*)

Return the value of the environment variable *key* as a string when it exists, otherwise *default*. *key* is a string. Keep in mind that because `getenv()` draws on `os.environ`, the mapping behind `getenv()` is likewise captured at import, so the function may not pick up later environment changes.

Under Unix, keys and values get decoded with [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding) and the `'surrogateescape'` error handler. Turn to `os.getenvb()` whenever you would prefer a different encoding.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

 os.getenvb(*key*, *default=None*)

Return the value of the environment variable *key* as bytes when it exists, otherwise *default*. *key* has to be bytes. Keep in mind that because `getenvb()` draws on `os.environb`, the mapping behind `getenvb()` is likewise captured at import, so the function may not pick up later environment changes.

`getenvb()` is only available if `supports_bytes_environ` is `True`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.2.

 os.get_exec_path(*env=None*)

Returns the list of directories that get searched for a named executable, much like a shell does, while launching a process. When supplied, *env* should be an environment variable dictionary in which to look up the PATH. By default, where *env* is `None`, `environ` is used.

Added in version 3.2.

 os.getegid()

Return the effective group id of the current process. This maps to the "set id" bit on the file being executed within the current process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.geteuid()

Return the current process's effective user id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.getgid()

Return the real group id of the current process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for more information.

 os.getgrouplist(*user*, *group*, */*)

Return a list of group ids that *user* belongs to. When *group* is absent from the list, it gets added; *group* is usually given as the group ID field from the password record for *user*, since otherwise that group ID would risk being left out.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.3.

 os.getgroups()

Return a list of supplemental group ids tied to the current process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Note

On macOS, the behavior of `getgroups()` is a little different from other Unix platforms. Should the Python interpreter have been built targeting a deployment of `10.5` or below, `getgroups()` hands back the effective group ids tied to the current user process; that list stops at a system-defined entry count, usually 16, and a privileged caller may alter it through `setgroups()`. When built with a deployment target above `10.5`, `getgroups()` returns the current group access list for the user tied to the effective user id of the process; the group access list may shift across the lifetime of the process, it stays unaffected by calls to `setgroups()`, and its length is not capped at 16. The deployment target value, `MACOSX_DEPLOYMENT_TARGET`, is obtainable with [`sysconfig.get_config_var()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_var).

 os.getlogin()

Return the name of the user logged in at the controlling terminal of the process. For most purposes, [`getpass.getuser()`](https://docs.python.org/3.14/library/getpass.html#getpass.getuser) proves more useful, since that one inspects the environment variables `LOGNAME` or `USERNAME` to determine who the user is, then falls back to `pwd.getpwuid(os.getuid())[0]` to obtain the login name of the current real user id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI.

 os.getpgid(*pid*)

Return the process group id of the process bearing process id *pid*. When *pid* is 0, the process group id of the current process comes back.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.getpgrp()

Return the id of the current process group.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

[Subject index](INDEX.md) · [Previous](os-pathlike-class.md) · [Continue](os-getpid-to-os-initgroups.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Parameters](os-ctermid-to-os-fsencode.md)
