# Python 3.7.0 beta 2 / library / imports and modules

[bpo-31333](https://bugs.python.org/issue?@action=redirect&bpo=31333): The `_abc` module gets added. This is a speedup module carrying C implementations covering assorted functions and methods within `abc`. Building an ABC subclass plus invoking `isinstance` or `issubclass` against an ABC subclass run as much as 1.5x faster. On top of that, this brings Python start-up as much as 10% faster. Be aware the fresh implementation conceals the internal registry and caches that were formerly reachable through the private attributes `_abc_registry`, `_abc_cache`, and `_abc_negative_cache`. Three debugging helper methods exist that may serve instead `_dump_registry`, `_abc_registry_clear`, and `_abc_caches_clear`.

[bpo-31787](https://bugs.python.org/issue?@action=redirect&bpo=31787): Corrected refleaks within `__init__()` methods across several modules. (Contributed by Oren Milman)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
