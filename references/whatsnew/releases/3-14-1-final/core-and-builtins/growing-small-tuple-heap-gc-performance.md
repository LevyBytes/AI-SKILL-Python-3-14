# Python 3.14.1 final / core and builtins / resolves regression gc performance affecting growing heap built largely

[gh-139951](https://github.com/python/cpython/issues/139951): Resolves a regression in GC performance affecting a growing heap built largely from small tuples.

  - Tallies the count of objects actually tracked rather than those merely trackable. That guarantees untracking tuples produces the intended reduction in GC overhead.

  - Refrains from tracking most untrackable tuples at creation time. That keeps large quantities of small tuples from provoking excessive GCs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
