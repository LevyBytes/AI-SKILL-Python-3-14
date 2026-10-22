# os: `os.setpgrp()`, `os.setpgid()`, `os.setpriority()`, `os.setregid()`, `os.setresgid()`, `os.setresuid()`, `os.setreuid()`, `os.getsid()`, `os.setsid()`, `os.setuid()`, `os.strerror()`, `os.supports_bytes_environ`, `os.umask()`

os.setpgrp()

Invoke whichever of the `setpgrp()` or `setpgrp(0, 0)` system calls is the implemented one (if either is). Consult the Unix manual for the semantics.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.setpgid(*pid*, *pgrp*, */*)

Invoke the `setpgid()` system call so that the process whose id is *pid* has its process group id set to the process group whose id is *pgrp*. Consult the Unix manual for the semantics.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.setpriority(*which*, *who*, *priority*)

Assign program scheduling priority. The *which* value is one of `PRIO_PROCESS`, `PRIO_PGRP`, or `PRIO_USER`, and *who* is read relative to *which* (a process identifier for `PRIO_PROCESS`, a process group identifier for `PRIO_PGRP`, and a user ID for `PRIO_USER`). When *who* is zero it stands for (respectively) the calling process, that process's process group, or that process's real user ID. *priority* spans the range -20 to 19. The default priority is 0; lower priorities yield more favorable scheduling.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.3.

 os.setregid(*rgid*, *egid*, */*)

Assign the calling process's real and effective group ids.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

 os.setresgid(*rgid*, *egid*, *sgid*, */*)

Assign the calling process's real, effective, and saved group ids.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

Added in version 3.2.

 os.setresuid(*ruid*, *euid*, *suid*, */*)

Assign the calling process's real, effective, and saved user ids.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

Added in version 3.2.

 os.setreuid(*ruid*, *euid*, */*)

Assign the calling process's real and effective user ids.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

 os.getsid(*pid*, */*)

Invoke the `getsid()` system call. Consult the Unix manual for the semantics.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.setsid()

Invoke the `setsid()` system call. Consult the Unix manual for the semantics.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.setuid(*uid*, */*)

Assign the calling process's user id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

 os.strerror(*code*, */*)

Give back the error message that goes with the error code in *code*. On platforms where `strerror()` hands back `NULL` for an unknown error number, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

 os.supports_bytes_environ

`True` when the environment's native OS type is bytes (so, `False` on Windows).

Added in version 3.2.

 os.umask(*mask*, */*)

Assign the current numeric umask and give back the prior umask.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for more information.

[Subject index](INDEX.md) · [Previous](os-setns-namespace-membership.md) · [Continue](os-uname-to-os-unshare.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Parameters](os-ctermid-to-os-fsencode.md)
