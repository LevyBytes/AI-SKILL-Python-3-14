# Python 3.13.0 alpha 3 / library / dis

[gh-112137](https://github.com/python/cpython/issues/112137): Alter [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) output so a missing line number prints as `–` in place of "None".

[gh-112137](https://github.com/python/cpython/issues/112137): Alter [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) output so jump targets show logical labels instead of offsets.

[gh-112962](https://github.com/python/cpython/issues/112962): Rather than fabricating fake `Instruction` objects to stand in for cache entries, the [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module functions now attach cache details onto the [`Instruction`](https://docs.python.org/3.14/library/dis.html#dis.Instruction) instance itself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
