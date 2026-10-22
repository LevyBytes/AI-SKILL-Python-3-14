# Python 3.12.0 alpha 1 / library / dataclasses

[gh-93521](https://github.com/python/cpython/issues/93521): Corrected a situation where dataclasses attempted to insert `__weakref__` into `__slots__` for a dataclass declaring `weakref_slot=True` even though one of its bases had already defined it. That had been raising a `TypeError` as the new class got created.

[bpo-35540](https://bugs.python.org/issue?@action=redirect&bpo=35540): Resolved a [`dataclasses.asdict()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.asdict) crash triggered when a [`collections.defaultdict`](https://docs.python.org/3.14/library/collections.html#collections.defaultdict) appears among the attributes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
