# Python 3.14.0 alpha 1 / library / inspect

[gh-115937](https://github.com/python/cpython/issues/115937): The extra preprocessing once applied to the `__signature__` attribute is gone; the code now merely tests whether it is an [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature) instance. Sergey B Kirpichev supplied the patch.

[gh-87106](https://github.com/python/cpython/issues/87106): [`inspect.Signature.bind()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.bind) now correctly deals with keyword arguments that share a name with positional-only arguments while a variadic keyword argument (e.g. `**kwargs`) is also in play.

[gh-122981](https://github.com/python/cpython/issues/122981): Repair [`inspect.getsource()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsource) for synthesized classes whose bases are written in Python (for instance enums).

[gh-122858](https://github.com/python/cpython/issues/122858): Mark `asyncio.iscoroutinefunction()` deprecated, preferring [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction).

[gh-123339](https://github.com/python/cpython/issues/123339): Repairs [`inspect.getsource()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsource) for classes living in the [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) and [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) (pure Python implementation) modules. [`inspect.getcomments()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcomments) now throws OSError rather than IndexError whenever a class's `__firstlineno__` value falls out of bound.

[gh-120381](https://github.com/python/cpython/issues/120381): Adjust [`inspect.ismethoddescriptor()`](https://docs.python.org/3.14/library/inspect.html#inspect.ismethoddescriptor) so it additionally verifies the absence of [`__delete__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__). Jan Kaliszewski provided the patch.

[gh-101552](https://github.com/python/cpython/issues/101552): Introduces an *annoation_format* parameter on [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature). Introduces an *quote_annotation_strings* parameter on [`inspect.Signature.format()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.format). That fresh capability is then leveraged to render annotations in signatures more cleanly within [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc). Jelle Zijlstra supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
