# What's New In Python 3.13 / typing — typing

### typing

- [**PEP 705**](https://peps.python.org/pep-0705/): Introduces [`ReadOnly`](https://docs.python.org/3.14/library/typing.html#typing.ReadOnly), a dedicated typing construct that flags a [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) item as read-only where type checkers are concerned.

- [**PEP 742**](https://peps.python.org/pep-0742/): Introduces [`TypeIs`](https://docs.python.org/3.14/library/typing.html#typing.TypeIs), a typing construct usable for telling a type checker how a type should be narrowed.

- Introduce [`NoDefault`](https://docs.python.org/3.14/library/typing.html#typing.NoDefault), a sentinel object that stands in for the defaults of certain parameters inside the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module. (Contributed by Jelle Zijlstra in [gh-116126](https://github.com/python/cpython/issues/116126).)

- Introduce [`get_protocol_members()`](https://docs.python.org/3.14/library/typing.html#typing.get_protocol_members), which yields the collection of members that define a [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol). (Contributed by Jelle Zijlstra in [gh-104873](https://github.com/python/cpython/issues/104873).)

- Introduce [`is_protocol()`](https://docs.python.org/3.14/library/typing.html#typing.is_protocol) for testing whether a given class is a [`Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol). (Contributed by Jelle Zijlstra in [gh-104873](https://github.com/python/cpython/issues/104873).)

- [`ClassVar`](https://docs.python.org/3.14/library/typing.html#typing.ClassVar) may now sit inside [`Final`](https://docs.python.org/3.14/library/typing.html#typing.Final), and the reverse nesting works too. (Contributed by Mehdi Drissi in [gh-89547](https://github.com/python/cpython/issues/89547).)

### typing

- Drop the `typing.io` and `typing.re` namespaces, which have carried a deprecation since Python 3.8. Whatever lived in those namespaces can be brought in straight from the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module. (Contributed by Sebastian Rittau in [gh-92871](https://github.com/python/cpython/issues/92871).)

- Drop the keyword-argument style of building [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) types, which carried a Python 3.11 deprecation. (Contributed by Tomas Roun in [gh-104786](https://github.com/python/cpython/issues/104786).)

[Subject index](INDEX.md) · [Previous source section](types.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](turtle.md) · [Next source section](unittest.md)
