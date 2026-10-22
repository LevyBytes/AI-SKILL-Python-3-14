# Python 3.14.0 beta 1 / tests / collections and iteration

[gh-109981](https://github.com/python/cpython/issues/109981): The test helper tallying the list of open file descriptors now applies the optimised `/dev/fd` approach across all Apple platforms instead of macOS alone. Doing so prevents crashes brought on by guarded file descriptors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
