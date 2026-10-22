# Python 3.9.0 alpha 6 / library / build and platforms

[bpo-38061](https://bugs.python.org/issue?@action=redirect&bpo=38061): Under FreeBSD, `os.closerange(fd_low, fd_high)` at this point invokes `closefrom(fd_low)` whenever *fd_high* meets or exceeds `sysconf(_SC_OPEN_MAX)`.

The original patch came from these four contributors: Ed Maste (emaste); also Conrad Meyer (cem); plus Kyle Evans (kevans); together with Kubilay Kocak (koobs): [https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=242274](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=242274)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
