# Python 3.5.3 release candidate 1 / library / re

[bpo-27122](https://bugs.python.org/issue?@action=redirect&bpo=27122): When an exception fires inside the block governed by a contextlib.ExitStack() and one of the exit-stack generators catches it and re-raises it as part of a chain, the original exception is no longer re-raised on exit; the newly chained one is allowed through instead. This sidesteps the [**PEP 479**](https://peps.python.org/pep-0479/) bug noted in issue25782.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
