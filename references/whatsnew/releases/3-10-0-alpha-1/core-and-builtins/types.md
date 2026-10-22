# Python 3.10.0 alpha 1 / core and builtins / types

[bpo-41780](https://bugs.python.org/issue?@action=redirect&bpo=41780): Corrects `__dir__()` on [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias). Batuhan Taskaya contributed the patch.

[bpo-40890](https://bugs.python.org/issue?@action=redirect&bpo=40890): A `mapping` attribute now appears on every dictionary view, exposing a [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) that wraps the underlying dictionary. Dennis Sweeney supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
