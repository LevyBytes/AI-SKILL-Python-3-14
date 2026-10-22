# Python 3.14.0 beta 2 / library / uuid

[gh-132710](https://github.com/python/cpython/issues/132710): Where feasible, make [`uuid.getnode()`](https://docs.python.org/3.14/library/uuid.html#uuid.getnode) yield an identical answer even between separate processes. Formerly the answer held constant only inside a single process. Patch by Bénédikt Tran.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
