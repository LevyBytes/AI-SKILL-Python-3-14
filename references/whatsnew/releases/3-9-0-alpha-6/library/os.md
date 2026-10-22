# Python 3.9.0 alpha 6 / library / os

[bpo-40138](https://bugs.python.org/issue?@action=redirect&bpo=40138): Repair the Windows build of [`os.waitpid()`](https://docs.python.org/3.14/library/os.html#os.waitpid) for an exit code above `INT_MAX >> 8`. The exit status is at this point read as an unsigned value.

[bpo-40094](https://bugs.python.org/issue?@action=redirect&bpo=40094): Introduce the [`os.waitstatus_to_exitcode()`](https://docs.python.org/3.14/library/os.html#os.waitstatus_to_exitcode) function, which turns a wait status into its exit code.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
