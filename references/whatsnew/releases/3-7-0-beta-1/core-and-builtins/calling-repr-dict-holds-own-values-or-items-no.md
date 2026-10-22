# Python 3.7.0 beta 1 / core and builtins / calling repr dict holds own values or items no

[bpo-18533](https://bugs.python.org/issue?@action=redirect&bpo=18533): Calling `repr()` on a dict that holds its own `values()` or `items()` no longer triggers `RecursionError`; OrderedDict behaves the same. Rather, `...` is used, just as with other recursive structures. Patch by Ben North.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
