# Python 3.12.0 beta 1 / library / dataclasses

[gh-103000](https://github.com/python/cpython/issues/103000): Boost the throughput of [`dataclasses.astuple()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.astuple) and [`dataclasses.asdict()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.asdict) whenever the contents consist of common Python types.

[gh-103000](https://github.com/python/cpython/issues/103000): Boost the performance of [`dataclasses.asdict()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.asdict) in the frequent case where *dict_factory* equals `dict`. David C Ellis wrote the patch.

[gh-103449](https://github.com/python/cpython/issues/103449): Repair a defect in how doc strings are produced inside [`dataclasses.dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
