# Python 3.13.0 alpha 2 / core and builtins / give tier uop interpreter small speed boost fetching oparg

[gh-112287](https://github.com/python/cpython/issues/112287): Give the Tier 2 (uop) interpreter a small speed boost by fetching `oparg` and `operand` solely when required. Likewise raise the trace size cap once more, this round to 512.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
