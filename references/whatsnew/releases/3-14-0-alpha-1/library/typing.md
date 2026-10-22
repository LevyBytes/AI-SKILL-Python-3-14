# Python 3.14.0 alpha 1 / library / typing

[gh-124787](https://github.com/python/cpython/issues/124787): Corrects [`typing.TypeAliasType`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType) when given a wrong `type_params` argument. It now throws a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) if some type parameter lacking a default comes after one carrying a default, and likewise if any element of the `type_params` tuple isn't a type parameter object.

[gh-118814](https://github.com/python/cpython/issues/118814): Repair the [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar) constructor for the case where name arrives as a keyword.

[gh-119180](https://github.com/python/cpython/issues/119180): Following [**PEP 749**](https://peps.python.org/pep-0749/), introduce these attributes that customize how annotation scopes are evaluated:

  - `evaluate_value` on [`typing.TypeAliasType`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType)

  - `evaluate_bound`, `evaluate_constraints`, and `evaluate_default` on [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar)

[gh-123448](https://github.com/python/cpython/issues/123448): Repaired a memory leak of [`typing.NoDefault`](https://docs.python.org/3.14/library/typing.html#typing.NoDefault) by relocating it into the static types array.

[gh-118772](https://github.com/python/cpython/issues/118772): In certain situations, a [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar) instance lacking a default may now come after another instance that also lacks one. Jelle Zijlstra wrote the patch.

[gh-118033](https://github.com/python/cpython/issues/118033): When a class subclasses [`typing.Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic), [`dataclasses.dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) previously skipped creating a `__weakref__` slot; that omission is now fixed.

[gh-114053](https://github.com/python/cpython/issues/114053): Repair a corner-case defect where [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) returned wrong results once type parameters within a class scope were shadowed by assignments in that class scope while `from __future__ import annotations` semantics were active. Alex Waygood wrote the patch.

[gh-118895](https://github.com/python/cpython/issues/118895): Assigning attributes onto [`typing.NoDefault`](https://docs.python.org/3.14/library/typing.html#typing.NoDefault) now raises [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) rather than [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[gh-124498](https://github.com/python/cpython/issues/124498): Keeps [`typing.TypeAliasType`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType) from being generic whenever `type_params` happens to be an empty tuple.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
