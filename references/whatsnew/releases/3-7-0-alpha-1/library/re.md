# Python 3.7.0 alpha 1 / library / re

[bpo-10076](https://bugs.python.org/issue?@action=redirect&bpo=10076): Within the re module, compiled regular expression objects and match objects now work with copy.copy() and copy.deepcopy() (being treated as atomic).

[bpo-30807](https://bugs.python.org/issue?@action=redirect&bpo=30807): signal.setitimer() can switch the timer off whenever it receives a very small value. Tiny values (1e-6 for example) count as valid non-zero values for setitimer(), which is defined as accepting microsecond-resolution intervals. Yet on some platforms our conversion routine could turn 1e-6 into a zero interval, which disables the timer rather than (re-)scheduling it.

[bpo-30375](https://bugs.python.org/issue?@action=redirect&bpo=30375): Warnings produced while a regular expression is compiled now consistently reference the line within the user's code. Formerly they might reference internals of the re module whenever they came from inside groups or conditionals.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
