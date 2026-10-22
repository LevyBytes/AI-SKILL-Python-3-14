# Python 3.9.0 alpha 1 / library / os

[bpo-37420](https://bugs.python.org/issue?@action=redirect&bpo=37420): Errors that surface while iterating across the `mask` argument of [`os.sched_setaffinity()`](https://docs.python.org/3.14/library/os.html#os.sched_setaffinity) are now handled properly. Brandt Bucher wrote the patch.

[bpo-37412](https://bugs.python.org/issue?@action=redirect&bpo=37412): On Windows the [`os.getcwdb()`](https://docs.python.org/3.14/library/os.html#os.getcwdb) function now relies on UTF-8 encoding in place of the ANSI code page; the reasoning lives in [**PEP 529**](https://peps.python.org/pep-0529/). On Windows the function has shed its deprecation.

[bpo-38265](https://bugs.python.org/issue?@action=redirect&bpo=38265): The *length* parameter of [`os.pread()`](https://docs.python.org/3.14/library/os.html#os.pread) now takes [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) rather than int.

[bpo-38493](https://bugs.python.org/issue?@action=redirect&bpo=38493): For `si_code`, the [`CLD_KILLED`](https://docs.python.org/3.14/library/os.html#os.CLD_KILLED) and [`CLD_STOPPED`](https://docs.python.org/3.14/library/os.html#os.CLD_STOPPED) values were added. Donghee Na supplied the patch.

[bpo-38378](https://bugs.python.org/issue?@action=redirect&bpo=38378): The *out* and *in* parameters of [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) became *out_fd* and *in_fd*.

[bpo-38713](https://bugs.python.org/issue?@action=redirect&bpo=38713): Introduced the [`os.P_PIDFD`](https://docs.python.org/3.14/library/os.html#os.P_PIDFD) constant, which one may hand to [`os.waitid()`](https://docs.python.org/3.14/library/os.html#os.waitid) in order to wait upon a Linux process file descriptor.

[bpo-38692](https://bugs.python.org/issue?@action=redirect&bpo=38692): Surfaced the Linux `pidfd_open` syscall under the name [`os.pidfd_open()`](https://docs.python.org/3.14/library/os.html#os.pidfd_open).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
