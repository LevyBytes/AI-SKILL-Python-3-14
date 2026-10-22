# Python 3.7.0 alpha 1 / library / build and platforms

[bpo-30205](https://bugs.python.org/issue?@action=redirect&bpo=30205): On Linux, getsockname() for unbound AF_UNIX sockets was corrected.

[bpo-28448](https://bugs.python.org/issue?@action=redirect&bpo=28448): Repaired the C-implemented asyncio.Future, which failed to operate under Windows.

[bpo-29728](https://bugs.python.org/issue?@action=redirect&bpo=29728): A fresh `socket.TCP_NOTSENT_LOWAT` (Linux 3.12) constant was added. Nathaniel J. Smith provided the patch.

[bpo-28075](https://bugs.python.org/issue?@action=redirect&bpo=28075): Added a check for ERROR_ACCESS_DENIED in the Windows version of os.stat(). Eryk Sun provided the patch.

[bpo-9146](https://bugs.python.org/issue?@action=redirect&bpo=9146): Repair a segmentation fault inside _hashopenssl whenever standard hash functions such as md5 are missing from the linked OpenSSL library, as happens in certain special FIPS-140 build environments.

[bpo-26273](https://bugs.python.org/issue?@action=redirect&bpo=26273): Introduced the `socket.TCP_CONGESTION` (Linux 2.6.13) plus `socket.TCP_USER_TIMEOUT` (Linux 2.6.37) constants. Omar Sandoval wrote this patch.

[bpo-29079](https://bugs.python.org/issue?@action=redirect&bpo=29079): Stopped an infinite loop from occurring inside pathlib.resolve() under Windows

[bpo-16255](https://bugs.python.org/issue?@action=redirect&bpo=16255): On Android, subprocess.Popen now invokes /system/bin/sh as its shell rather than /bin/sh.

[bpo-30418](https://bugs.python.org/issue?@action=redirect&bpo=30418): Under Windows, subprocess.Popen.communicate() now likewise disregards EINVAL from stdin.write() whenever the child is alive yet has shut its end of the pipe.

[bpo-30605](https://bugs.python.org/issue?@action=redirect&bpo=30605): Compiling a bytes instance carrying a misplaced inline modifier no longer triggers a BytesWarning from re.compile(). Roy Williams wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
