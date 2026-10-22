# Python 3.9.0 alpha 6 / library / subprocess

[bpo-38061](https://bugs.python.org/issue?@action=redirect&bpo=38061): Speed up the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module under FreeBSD through `closefrom()`. One `close(fd)` syscall costs little, yet once `sysconf(_SC_OPEN_MAX)` grows large, the loop that runs `close(fd)` per file descriptor may consume several milliseconds.

The FreeBSD performance workaround used to involve loading and mounting the fdescfs kernel module, which is off by default.

The original patch came from these four contributors: Ed Maste (emaste); also Conrad Meyer (cem); plus Kyle Evans (kevans); together with Kubilay Kocak (koobs): [https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=242274](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=242274)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
