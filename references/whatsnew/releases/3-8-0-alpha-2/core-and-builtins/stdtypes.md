# Python 3.8.0 alpha 2 / core and builtins / stdtypes

[bpo-33989](https://bugs.python.org/issue?@action=redirect&bpo=33989): Repair a potential [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) crash while sorting objects whose `ob_type->tp_richcompare == NULL`. Patch by Zackery Spytz.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
