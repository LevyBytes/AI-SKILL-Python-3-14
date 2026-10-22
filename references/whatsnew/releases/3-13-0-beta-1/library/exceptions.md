# Python 3.13.0 beta 1 / library / exceptions

[gh-116871](https://github.com/python/cpython/issues/116871): Name suggestions for [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) and [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) now surface underscored names solely when the original name itself was underscored.

[gh-114053](https://github.com/python/cpython/issues/114053): Eliminates a spurious [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) raised by [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) against a class that relied on [**PEP 695**](https://peps.python.org/pep-0695/) type parameters within a module carrying `from __future__ import annotations` at its top. Alex Waygood provided the patch.

[gh-117995](https://github.com/python/cpython/issues/117995): No [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) is emitted now when a [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) of parameters binds indexed, nameless placeholders. Refer as well to [gh-100668](https://github.com/python/cpython/issues/100668).

[gh-118418](https://github.com/python/cpython/issues/118418): A [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) now fires whenever you omit a value for the new *type_params* parameter of `typing._eval_type()` or `typing.ForwardRef._evaluate()`. (Reaching for either of these private, undocumented functions is already inadvisable, yet skipping a value for the `type_params` parameter can yield wrong behaviour on Python 3.12 or later.)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
