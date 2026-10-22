# os — os.setns namespace membership

Beginning with Linux 5.8, *fd* may be a PID file descriptor handed back by `pidfd_open()`. When that is the case, `setns()` joins the calling thread to one or more of the same namespaces as the thread that *fd* points at. This obeys whatever limits *nstype* imposes, that being a bit mask that ORs together one or more of the CLONE_NEW* constants, for example `setns(fd, os.CLONE_NEWUTS | os.CLONE_NEWPID)`. The caller's memberships in any namespaces left unspecified stay as they were.

*fd* may be any object carrying a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method, or else a raw file descriptor.

The example below joins the thread to the `init` process's network namespace:

```python
fd = os.open("/proc/1/ns/net", os.O_RDONLY)
os.setns(fd, os.CLONE_NEWNET)
os.close(fd)

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.0 with glibc >= 2.14.

Added in version 3.12.

See also

The `unshare()` function.

[Subject index](INDEX.md) · [Continue](os-setpgrp-to-os-umask.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: os.setns namespace membership](os-putenv-to-os-setns.md) · [Preceding source contract and version conditions](os-putenv-to-os-setns.md)
