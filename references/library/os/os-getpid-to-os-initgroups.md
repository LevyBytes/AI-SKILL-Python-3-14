# os: Process identity, priority and user/group credentials

os.getpid()

Return the current process id.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for more information.

 os.getppid()

Return the parent's process id. Once the parent process has exited, under Unix the id returned belongs to the init process (1); under Windows it remains the same id, which may already have been reused by another process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI.

Changed in version 3.2: Added support for Windows.

 os.getpriority(*which*, *who*)

Get the program scheduling priority. The *which* value is one of `PRIO_PROCESS`, `PRIO_PGRP`, or `PRIO_USER`, while *who* is read relative to *which* (a process identifier for `PRIO_PROCESS`, a process group identifier for `PRIO_PGRP`, and a user ID for `PRIO_USER`). A *who* value of zero stands, in turn, for the calling process itself, that process's process group, or that process's real user ID.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.3.

 os.PRIO_PROCESS

 os.PRIO_PGRP

 os.PRIO_USER

Parameters for the `getpriority()` and `setpriority()` functions.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.3.

 os.PRIO_DARWIN_THREAD

 os.PRIO_DARWIN_PROCESS

 os.PRIO_DARWIN_BG

 os.PRIO_DARWIN_NONUI

Parameters for the `getpriority()` and `setpriority()` functions.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): macOS

Added in version 3.12.

 os.getresuid()

Return the current process's real, effective, and saved user ids as a tuple (ruid, euid, suid).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.2.

 os.getresgid()

Return the current process's real, effective, and saved group ids as a tuple (rgid, egid, sgid).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.2.

 os.getuid()

Return the current process's real user id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for more information.

 os.initgroups(*username*, *gid*, */*)

Call the system `initgroups()` so the group access list is initialized with all the groups that the given username belongs to, plus the specified group id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](os-getenv-to-os-getpgrp.md) · [Continue](os-putenv-to-os-setns.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Parameters](os-ctermid-to-os-fsencode.md)
