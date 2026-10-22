# Python 3.10.0 beta 1 / library / collections and iteration

[bpo-41559](https://bugs.python.org/issue?@action=redirect&bpo=41559): [**PEP 612**](https://peps.python.org/pep-0612/) now lives entirely in Python; builtin `types.GenericAlias` objects no longer carry `typing.ParamSpec` within `__parameters__` (apart from the `GenericAlias` belonging to `collections.abc.Callable`). Because of this, formerly invalid `ParamSpec` usages (for instance `list[P]`) that did function in earlier Python 3.10 alpha builds will now raise `TypeError` while substitution happens.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
