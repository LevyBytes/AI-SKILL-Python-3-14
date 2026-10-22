# Python 3.5.4 release candidate 1 / library / build and platforms

[bpo-30418](https://bugs.python.org/issue?@action=redirect&bpo=30418): Under Windows, subprocess.Popen.communicate() now likewise ignores EINVAL from stdin.write() when the child process keeps running but has shut the pipe.

[bpo-30205](https://bugs.python.org/issue?@action=redirect&bpo=30205): Repair getsockname() for AF_UNIX sockets that are unbound on Linux.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
