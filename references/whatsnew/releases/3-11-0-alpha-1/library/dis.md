# Python 3.11.0 alpha 1 / library / dis

[bpo-45168](https://bugs.python.org/issue?@action=redirect&bpo=45168): Adjusted [`dis.dis()`](https://docs.python.org/3.14/library/dis.html#dis.dis) so its output skips op arg values that stay unresolved because `co_consts`, `co_names`, and similar data were absent. Formerly the oparg got echoed back in the value column, which adds no clarity and may mislead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
