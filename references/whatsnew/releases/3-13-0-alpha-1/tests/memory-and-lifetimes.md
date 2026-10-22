# Python 3.13.0 alpha 1 / tests / memory and lifetimes

[gh-109739](https://github.com/python/cpython/issues/109739): regrtest: Sorted out the reference leak check on Windows. The load tracker is now switched off on Windows whenever the reference leak check mode (-R option) runs. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
