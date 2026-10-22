# Python 3.13.0 alpha 1 / library / types

[gh-101162](https://github.com/python/cpython/issues/101162): Disallowed calling `builtins.issubclass()` when [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias) is supplied as its first argument.

[gh-109174](https://github.com/python/cpython/issues/109174): Bring [`types.SimpleNamespace`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace) into the supported set for [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace).

[gh-107576](https://github.com/python/cpython/issues/107576): Adjust [`types.get_original_bases()`](https://docs.python.org/3.14/library/types.html#types.get_original_bases) so it hands back `__orig_bases__` solely when that attribute sits on `cls` directly. James Hilton-Balfe contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
