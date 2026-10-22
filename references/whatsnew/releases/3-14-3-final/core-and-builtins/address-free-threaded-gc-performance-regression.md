# Python 3.14.3 final / core and builtins / address free threaded gc performance regression

[gh-142531](https://github.com/python/cpython/issues/142531): Address a free-threaded GC performance regression. Where many untracked tuples exist, the GC fired too frequently and performance suffered. The remedy folds untracked tuples into the "long lived" object tally. The count of frozen objects is now part of that figure as well, since the free-threaded GC has to scan them too.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
