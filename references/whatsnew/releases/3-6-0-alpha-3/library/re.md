# Python 3.6.0 alpha 3 / library / re

[bpo-27177](https://bugs.python.org/issue?@action=redirect&bpo=27177): Within the re module, match objects now accept index-like objects when used as group indices. Jeroen Demeyer and Xiang Zhang supplied the underlying patches.

[bpo-27122](https://bugs.python.org/issue?@action=redirect&bpo=27122): If an exception is thrown inside the context handled by a contextlib.ExitStack() and one of the exit-stack generators traps it and re-raises it in a chain, the original exception is not re-raised on exit — the newly chained one is allowed through instead. This sidesteps the [**PEP 479**](https://peps.python.org/pep-0479/) bug detailed in issue25782.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
