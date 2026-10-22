# Python 3.14.0 alpha 4 / library / sys monitoring

[gh-122548](https://github.com/python/cpython/issues/122548): Two new local events join sys.monitoring, `BRANCH_LEFT` and `BRANCH_RIGHT`. With them, each arm of a branch can be turned off on its own, which ought to massively boost the performance of branch-level coverage tools. The former branch event, `BRANCH`, now carries a deprecation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
