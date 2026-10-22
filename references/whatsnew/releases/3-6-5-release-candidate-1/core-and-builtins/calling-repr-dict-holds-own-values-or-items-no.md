# Python 3.6.5 release candidate 1 / core and builtins / calling repr dict holds own values or items no

[bpo-18533](https://bugs.python.org/issue?@action=redirect&bpo=18533): Calling `repr()` on a dict that holds its own `values()` or `items()` no longer triggers `RecursionError`; the same applies to OrderedDict. The output now shows `...`, just like other self-referential structures. Ben North supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
