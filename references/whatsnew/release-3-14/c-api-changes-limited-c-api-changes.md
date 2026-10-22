# What's new in Python 3.14 / C API changes / Limited C API changes

### Limited C API changes

- Beginning with limited C API version 3.14, both [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) and [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) are now realized as opaque function calls so that implementation details stay hidden. (Contributed by Victor Stinner in [gh-120600](https://github.com/python/cpython/issues/120600) and [gh-124127](https://github.com/python/cpython/issues/124127).)

- Drop the [`PySequence_Fast_GET_SIZE`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Fast_GET_SIZE), [`PySequence_Fast_GET_ITEM`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Fast_GET_ITEM), and [`PySequence_Fast_ITEMS`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Fast_ITEMS) macros out of the limited C API, where they had always been broken. (Contributed by Victor Stinner in [gh-91417](https://github.com/python/cpython/issues/91417).)

[Subject index](INDEX.md) · [Previous source section](unique-reference-and-free-threading-apis.md) · [Next source section](c-api-changes-removed-c-apis.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md)
