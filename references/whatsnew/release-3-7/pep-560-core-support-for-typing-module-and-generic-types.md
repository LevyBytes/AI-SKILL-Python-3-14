# What's New In Python 3.7 / PEP 560: Core Support for `typing` module and Generic Types — typing

### PEP 560: Core Support for `typing` module and Generic Types

At the outset [**PEP 484**](https://peps.python.org/pep-0484/) was crafted so that it would add *no* changes whatsoever to the core CPython interpreter. These days type hints and the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module see heavy use among the community, so that limitation is lifted. This PEP adds two special methods [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) and [`__mro_entries__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__mro_entries__), which most classes and special constructs in `typing` now rely on. Consequently, various type operations got as much as 7 times faster, generic types work free of metaclass clashes, and a number of longstanding `typing` module bugs are resolved.

See also

[**PEP 560**](https://peps.python.org/pep-0560/) — Core support for typing module and generic types

PEP written and implemented by Ivan Levkivskyi

[Subject index](INDEX.md) · [Previous source section](pep-565-show-deprecationwarning-in-main.md) · [Next source section](pep-552-hash-based-pyc-files.md) · [Release/subject declaration](summary-release-highlights.md)
