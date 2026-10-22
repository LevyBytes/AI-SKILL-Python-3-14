# Python 3.5.4 release candidate 1 / library / re

[bpo-30375](https://bugs.python.org/issue?@action=redirect&bpo=30375): Warnings raised while a regular expression is compiled now always indicate the line within the user code. Formerly they could indicate the internals of the re module when raised from inside groups or conditionals.

[bpo-30807](https://bugs.python.org/issue?@action=redirect&bpo=30807): signal.setitimer() can switch the timer off if it is handed a very small value. Very small values (1e-6 for instance) are legitimate non-zero values for setitimer(), whose spec describes microsecond-resolution intervals. On certain platforms, however, our conversion routine might turn 1e-6 into a zero interval, which switches the timer off rather than (re-)scheduling it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
