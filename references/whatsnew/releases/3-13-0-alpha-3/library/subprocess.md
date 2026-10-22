# Python 3.13.0 alpha 3 / library / subprocess

[gh-113117](https://github.com/python/cpython/issues/113117): On platforms that expose `posix_spawn_file_actions_addclosefrom_np`, the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module is now able to invoke [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) together with `close_fds=True`. Jakub Kulik wrote the patch.

[gh-112736](https://github.com/python/cpython/issues/112736): To enable use within cross-platform build setups, the del-safe symbols inside `subprocess` were reorganized.

[gh-112334](https://github.com/python/cpython/issues/112334): Repair a performance regression introduced in 3.12's [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) on Linux, where a logic bug stopped it from taking the fast-path `vfork()` system call in situations where it could have, dropping back to the safe yet slower `fork()` instead.

A second 3.12.0 potential security bug was also fixed. When `extra_groups=[]` was handed to [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) or related APIs, the child process failed to issue the underlying `setgroups(0, NULL)` system call clearing the groups list before reaching `exec()`.

Inspecting the code while repairing the first bug is what surfaced this one.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
