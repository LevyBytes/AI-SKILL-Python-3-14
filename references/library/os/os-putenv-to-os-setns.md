# os: `os.putenv()`, `os.setegid()`, `os.seteuid()`, `os.setgid()`, `os.setgroups()`, `os.setns()`

os.putenv(*key*, *value*, */*)

Set the environment variable named *key* to the string *value*. Environment changes of this kind affect subprocesses launched with `os.system()`, `popen()` or `fork()` and `execv()`.

Assignments to items in `os.environ` get translated automatically into matching calls to `putenv()`; calls to `putenv()`, however, do not update `os.environ`, which is why assigning to items of `os.environ` is actually the better choice. The same goes for `getenv()` and `getenvb()`, whose implementations draw respectively on `os.environ` and `os.environb`.

See also the `os.reload_environ()` function.

Note

On certain platforms, FreeBSD and macOS among them, setting `environ` can produce memory leaks. Consult the system documentation covering `putenv()`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.putenv` with arguments `key`, `value`.

Changed in version 3.9: The function is now always available.

 os.setegid(*egid*, */*)

Set the current process's effective group id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

 os.seteuid(*euid*, */*)

Set the current process's effective user id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

 os.setgid(*gid*, */*)

Set the current process' group id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

 os.setgroups(*groups*, */*)

Set the list of supplemental group ids tied to the current process to *groups*. *groups* has to be a sequence, with each element being an integer that identifies a group. As a rule, this operation is open only to the superuser.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Note

On macOS, the length of *groups* must stay within the system-defined maximum number of effective group ids, usually 16. Refer to the documentation for `getgroups()` regarding cases where it may not return the same group list that calling setgroups() set.

 os.setns(*fd*, *nstype=0*)

Reassociate the current thread with a Linux namespace. Refer to the *[setns(2)](https://manpages.debian.org/setns(2))* and *[namespaces(7)](https://manpages.debian.org/namespaces(7))* man pages for more details.

When *fd* points at a `/proc/*pid*/ns/` link, `setns()` reassociates the calling thread with whatever namespace that link is tied to; you can set *nstype* to one of the CLONE_NEW* constants so as to constrain the operation (`0` means no constraints).

[Subject index](INDEX.md) · [Previous](os-getpid-to-os-initgroups.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Parameters](os-ctermid-to-os-fsencode.md) · [Required continuation of the source contract](os-setns-namespace-membership.md)
