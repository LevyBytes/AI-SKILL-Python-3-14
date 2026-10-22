# Python 3.13.0 alpha 1 / c api / import

[gh-105922](https://github.com/python/cpython/issues/105922): The [`PyImport_AddModuleRef()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AddModuleRef) function is added; it parallels [`PyImport_AddModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AddModule) but returns a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) rather than a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). Victor Stinner wrote the patch.

[gh-105396](https://github.com/python/cpython/issues/105396): The [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock) function, which has merely aliased [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule) ever since Python 3.3, is now deprecated. Victor Stinner wrote the patch.

[gh-109521](https://github.com/python/cpython/issues/109521): When [`PyImport_GetImporter()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_GetImporter) cannot obtain [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) or [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache), or finds they are not respectively a list and a dict, it now raises RuntimeError. Earlier it might quietly hand back NULL in rare situations, crash, or raise SystemError when those attributes carried the wrong type.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
