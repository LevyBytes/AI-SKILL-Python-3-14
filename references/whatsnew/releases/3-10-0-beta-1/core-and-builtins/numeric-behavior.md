# Python 3.10.0 beta 1 / core and builtins / numeric behavior

[bpo-43933](https://bugs.python.org/issue?@action=redirect&bpo=43933): Assign frame.f_lineno the line number belonging to the "with" kweyword as the call to `__exit__` runs.

[bpo-43933](https://bugs.python.org/issue?@action=redirect&bpo=43933): Where a frame's current position carries no line number, set the f_lineno attribute to None rather than -1, in keeping with PEP 626. Ordinarily this should be impossible, though it may arise under some unusual circumstances.

[bpo-42739](https://bugs.python.org/issue?@action=redirect&bpo=42739): How line number tables are represented internally was reworked so sentinels are no longer relied on, and the out-of-process API routine `PyLineTable_InitAddressRange` gained an explicit length parameter. The result is sturdier treatment of those line number tables under certain conditions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
