# subprocess: Popen working-directory and platform-specific options

Changed in version 3.6: under POSIX, *cwd* now takes a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: under Windows, *cwd* now takes a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.8: under Windows, *cwd* now takes a bytes object.

When *restore_signals* holds true (this is the default), every signal that Python switched to SIG_IGN gets reset to SIG_DFL inside the child before the exec runs. At present the affected set covers the SIGPIPE, SIGXFZ and SIGXFSZ signals. (POSIX only)

Changed in version 3.2: *restore_signals* was added.

When *start_new_session* is true, the child process issues the `setsid()` system call ahead of launching the subprocess.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX

Changed in version 3.2: *start_new_session* was added.

When *process_group* holds a non-negative integer, the child process issues the `setpgid(0, value)` system call ahead of launching the subprocess.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX

Changed in version 3.11: *process_group* was added.

When *group* differs from `None`, the child process invokes the setregid() system call before launching the subprocess. A string value gets resolved through [`grp.getgrnam()`](https://docs.python.org/3.14/library/grp.html#grp.getgrnam), after which the `gr_gid` field supplies the value used. An integer value is forwarded unchanged. (POSIX only)

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX

Added in version 3.9.

When *extra_groups* differs from `None`, the child process invokes the setgroups() system call before launching the subprocess. Any strings listed in *extra_groups* get resolved through [`grp.getgrnam()`](https://docs.python.org/3.14/library/grp.html#grp.getgrnam), after which the matching `gr_gid` values are used. Integer entries are forwarded unchanged. (POSIX only)

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX

Added in version 3.9.

When *user* differs from `None`, the child process invokes the setreuid() system call before launching the subprocess. A string value gets resolved through [`pwd.getpwnam()`](https://docs.python.org/3.14/library/pwd.html#pwd.getpwnam), after which the `pw_uid` field supplies the value used. An integer value is forwarded unchanged. (POSIX only)

Note

Passing *user* leaves any current supplementary group memberships in place! For security reasons, the caller should additionally pass `extra_groups=()` so the child process sheds those group memberships.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX

Added in version 3.9.

When *umask* is not a negative value, the child process issues the umask() system call ahead of launching the subprocess.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): POSIX

Added in version 3.9.

When *env* differs from `None`, it has to be a mapping that lays out the environment variables for the spawned process; these take the place of the default behavior, which inherits the environment of the current process. Such a mapping may go from str to str on every platform, or from bytes to bytes on POSIX platforms, in the same spirit as [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ) or [`os.environb`](https://docs.python.org/3.14/library/os.html#os.environb).

Note

When you supply *env*, it has to carry whatever variables the program needs in order to run. Under Windows, launching a [side-by-side assembly](https://en.wikipedia.org/wiki/Side-by-Side_Assembly) requires that the *env* you provide **must** include a valid `%SystemRoot%`.

When *encoding* or *errors* is given, or when *text* is true, the *stdin*, *stdout* and *stderr* file objects open in text mode using the *encoding* and *errors* you supplied, just as the Frequently Used Arguments section above explains. The *universal_newlines* argument means the same thing as *text* and remains for backwards compatibility. Without those options, file objects open in binary mode by default.

Added in version 3.6: *encoding* and *errors* were added.

Added in version 3.7: *text* arrived as an easier-to-read alias standing in for *universal_newlines*.

When supplied, *startupinfo* is a `STARTUPINFO` object that gets handed to the underlying `CreateProcess` function.

When supplied, *creationflags* may consist of one or several of these flags:

- `CREATE_NEW_CONSOLE`

- `CREATE_NEW_PROCESS_GROUP`

- `ABOVE_NORMAL_PRIORITY_CLASS`

-

[Subject index](INDEX.md) · [Continue](popen-creation-flags-and-stream-buffers.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: subprocess.Popen](subprocess-popen-class.md) · [Owning module, declaration or section: Popen Constructor](popen-constructor.md) · [Preceding source contract and version conditions](windows-executable-bytes-and-pathlike-support.md)
