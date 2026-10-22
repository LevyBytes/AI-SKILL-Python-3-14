# Python 3.13.0 beta 1 / library / inspect

[gh-82062](https://github.com/python/cpython/issues/82062): Corrects [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) so it handles parameter defaults properly for methods in extension modules that reference names defined within the module namespace.

[gh-118013](https://github.com/python/cpython/issues/118013): Corrects a regression that [gh-103193](https://github.com/python/cpython/issues/103193) had introduced, whereby invoking [`inspect.getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static) against an instance would keep a strong reference alive to that instance's class inside an internal cache belonging to the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module. The result was surprising memory growth whenever the class had been built dynamically, the class itself retained strong references to other large objects, and that cache happened to be the only remaining strong reference to the class. Patching the regression slows `getattr_static()` somewhat, yet the routine remains far quicker than the Python 3.11 version. Alex Waygood authored the patch.

[gh-118404](https://github.com/python/cpython/issues/118404): Repair [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) for callables that cannot be compared.

[gh-118402](https://github.com/python/cpython/issues/118402): Repair [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) on the object returned by a [`functools.cmp_to_key()`](https://docs.python.org/3.14/library/functools.html#functools.cmp_to_key) call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
