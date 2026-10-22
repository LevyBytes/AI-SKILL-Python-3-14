# Python 3.8.0 alpha 1 / core and builtins / sys

[bpo-30156](https://bugs.python.org/issue?@action=redirect&bpo=30156): The C routine `property_descr_get()` relies on a ?cached? tuple to speed up function calls. That tuple, however, can be uncovered while running in debug mode via [`sys.getobjects()`](https://docs.python.org/3.14/library/sys.html#sys.getobjects). Drop the optimization; the benefit is marginal and it has produced 3 separate crashes over recent years.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
