# What's New In Python 3.3 / SimpleNamespace end - types

A fresh type arrives in Python alongside the `sys.implementation` work: [`types.SimpleNamespace`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace). Where a mapping-style namespace such as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) keys its contents, `SimpleNamespace` reaches its members by attribute, the way [`object`](https://docs.python.org/3.14/library/functions.html#object) does. The difference from `object` is that a `SimpleNamespace` instance permits writing. Ordinary attribute access therefore lets you insert, drop, and edit entries within the namespace.

See also

[**PEP 421**](https://peps.python.org/pep-0421/) - Adding sys.implementation

Authoring of the PEP, and its implementation, were both the work of Eric Snow.

[Subject index](INDEX.md) · [Next source section](using-importlib-as-the-implementation-of-import.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-421-adding-sys-implementation.md) · [Preceding release/subject continuation](pep-421-adding-sys-implementation.md)
