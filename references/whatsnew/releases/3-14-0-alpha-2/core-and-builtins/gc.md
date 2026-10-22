# Python 3.14.0 alpha 2 / core and builtins / gc

[gh-126312](https://github.com/python/cpython/issues/126312): On the free-threaded build, a crash that struck during garbage collection of an object frozen via [`gc.freeze()`](https://docs.python.org/3.14/library/gc.html#gc.freeze) has been corrected.

[gh-125859](https://github.com/python/cpython/issues/125859): A crash affecting the free threading build, triggered whenever [`gc.get_objects()`](https://docs.python.org/3.14/library/gc.html#gc.get_objects) or [`gc.get_referrers()`](https://docs.python.org/3.14/library/gc.html#gc.get_referrers) runs while garbage collection is still underway, has been resolved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
