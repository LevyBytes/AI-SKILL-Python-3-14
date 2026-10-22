# Python 3.10.0 alpha 3 / core and builtins / stdtypes

[bpo-42233](https://bugs.python.org/issue?@action=redirect&bpo=42233): Let `GenericAlias` objects participate in [union type expressions](https://docs.python.org/3.14/library/stdtypes.html#types-union). Expressions such as `list[int] | dict[float, str]`, which formerly raised a `TypeError`, now work. The change also corrects union type expressions failing to de-duplicate `GenericAlias` objects. (Ken Jin landed this in [bpo-42233](https://bugs.python.org/issue?@action=redirect&bpo=42233).)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
