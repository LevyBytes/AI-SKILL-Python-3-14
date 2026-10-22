# Python 3.14.4 final / core and builtins / collections and iteration

[gh-148144](https://github.com/python/cpython/issues/148144): Set `_PyInterpreterFrame.visited` during interpreter-frame copying so that incremental GC never reads an uninitialized byte out of generator and frame-object copies.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
