# Python 3.12.0 alpha 1 / library / copy

[gh-94383](https://github.com/python/cpython/issues/94383): `xml.etree`: The `ElementTree.Element.copy()` method of the pure Python implementation, deprecated back in Python 3.10, is removed; reach for the [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) function instead. The C version of `xml.etree` carries no `copy()` method, only a `__copy__()` method. Victor Stinner wrote the patch.

[gh-90494](https://github.com/python/cpython/issues/90494): [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) along with [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy) will now consistently raise a TypeError whenever `__reduce__()` hands back a 6-element tuple, rather than quietly skipping that sixth item or yielding a wrong result.

[gh-93820](https://github.com/python/cpython/issues/93820): Repaired a regression triggered when [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy)-ing an [`enum.Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) that carries several flag members.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
