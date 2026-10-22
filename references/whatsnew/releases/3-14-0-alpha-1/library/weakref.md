# Python 3.14.0 alpha 1 / library / weakref

[gh-123089](https://github.com/python/cpython/issues/123089): Hardens [`weakref.WeakSet`](https://docs.python.org/3.14/library/weakref.html#weakref.WeakSet) against being mutated concurrently while iteration is underway. Kumar Aditya wrote the patch.

[gh-89967](https://github.com/python/cpython/issues/89967): Render [`WeakKeyDictionary`](https://docs.python.org/3.14/library/weakref.html#weakref.WeakKeyDictionary) and [`WeakValueDictionary`](https://docs.python.org/3.14/library/weakref.html#weakref.WeakValueDictionary) safe when other threads mutate them concurrently. Patch by Kumar Aditya.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
