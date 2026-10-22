# Python 3.14.0 beta 2 / library / typing

[gh-133960](https://github.com/python/cpython/issues/133960): Streamline and strengthen [`typing.evaluate_forward_ref()`](https://docs.python.org/3.14/library/typing.html#typing.evaluate_forward_ref). It no longer throws errors for some invalid types. Across several scenarios it can now resolve forward references that formerly went unsupported.

[gh-133701](https://github.com/python/cpython/issues/133701): Repair the bug where [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) classes declared under `from __future__ import annotations` and subclassing another `TypedDict` ended up with a wrong `__annotations__` attribute.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
