# Python 3.13.0 alpha 2 / library / wsgiref

[gh-111768](https://github.com/python/cpython/issues/111768): The `__all__` listing now properly exports [`wsgiref.util.is_hop_by_hop()`](https://docs.python.org/3.14/library/wsgiref.html#wsgiref.util.is_hop_by_hop).

[gh-66425](https://github.com/python/cpython/issues/66425): Strip out the logic that set the REMOTE_HOST header in the wsgiref module, given that it cannot be reached. That header serves performance goals, which the wsgiref module has no need for.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
