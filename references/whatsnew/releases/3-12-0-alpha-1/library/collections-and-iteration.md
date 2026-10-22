# Python 3.12.0 alpha 1 / library / collections and iteration

[gh-98363](https://github.com/python/cpython/issues/98363): Introduced itertools.batched() for grouping data into lists of a stated length, where the final list may run shorter than the rest.

[gh-91162](https://github.com/python/cpython/issues/91162): Permit an unpacked arbitrary-length tuple to be split across `TypeVar` and `TypeVarTuple` parameters. As an illustration:

  - `A[T, *Ts][*tuple[int, ...]]` -> `A[int, *tuple[int, ...]]`

  - `A[*Ts, T][*tuple[int, ...]]` -> `A[*tuple[int, ...], int]`

[gh-95105](https://github.com/python/cpython/issues/95105): `wsgiref.types.InputStream.__iter__()` ought to hand back `Iterator[bytes]` instead of `Iterable[bytes]`. Shantanu Jain wrote the patch.

[gh-94343](https://github.com/python/cpython/issues/94343): The attributes of `reprlib.Repr` may now be set while the object is being initialized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
