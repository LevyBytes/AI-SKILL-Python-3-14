# What's New In Python 3.9 / os — os

### os

The [`CLD_KILLED`](https://docs.python.org/3.14/library/os.html#os.CLD_KILLED) and [`CLD_STOPPED`](https://docs.python.org/3.14/library/os.html#os.CLD_STOPPED) values were added for use with `si_code`. (Contributed by Donghee Na in [bpo-38493](https://bugs.python.org/issue?@action=redirect&bpo=38493).)

The Linux-only [`os.pidfd_open()`](https://docs.python.org/3.14/library/os.html#os.pidfd_open) ([bpo-38692](https://bugs.python.org/issue?@action=redirect&bpo=38692)) and [`os.P_PIDFD`](https://docs.python.org/3.14/library/os.html#os.P_PIDFD) ([bpo-38713](https://bugs.python.org/issue?@action=redirect&bpo=38713)) were exposed so processes can be managed via file descriptors.

The [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv) function can now be used on Windows too. (Contributed by Victor Stinner in [bpo-39413](https://bugs.python.org/issue?@action=redirect&bpo=39413).)

Both the [`os.putenv()`](https://docs.python.org/3.14/library/os.html#os.putenv) and [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv) functions are now present at all times. (Contributed by Victor Stinner in [bpo-39395](https://bugs.python.org/issue?@action=redirect&bpo=39395).)

A new [`os.waitstatus_to_exitcode()`](https://docs.python.org/3.14/library/os.html#os.waitstatus_to_exitcode) function was added that translates a wait status into an exit code. (Contributed by Victor Stinner in [bpo-40094](https://bugs.python.org/issue?@action=redirect&bpo=40094).)

[Subject index](INDEX.md) · [Previous source section](nntplib.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)
