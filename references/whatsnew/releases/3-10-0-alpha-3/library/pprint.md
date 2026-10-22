# Python 3.10.0 alpha 3 / library / pprint

[bpo-28850](https://bugs.python.org/issue?@action=redirect&bpo=28850): Repair [`pprint.PrettyPrinter.format()`](https://docs.python.org/3.14/library/pprint.html#pprint.PrettyPrinter.format) overrides that were being skipped for the contents of small containers. The `pprint._safe_repr()` function was removed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
