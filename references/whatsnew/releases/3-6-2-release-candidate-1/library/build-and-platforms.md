# Python 3.6.2 release candidate 1 / library / build and platforms

[bpo-30205](https://bugs.python.org/issue?@action=redirect&bpo=30205): On Linux, repair getsockname() for AF_UNIX sockets that are unbound.

[bpo-30605](https://bugs.python.org/issue?@action=redirect&bpo=30605): re.compile() will no longer emit a BytesWarning while compiling a bytes instance that carries a misplaced inline modifier. Roy Williams wrote the patch.

[bpo-30418](https://bugs.python.org/issue?@action=redirect&bpo=30418): Under Windows, subprocess.Popen.communicate() now likewise disregards EINVAL from stdin.write() when the child process keeps running yet has shut the pipe.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
