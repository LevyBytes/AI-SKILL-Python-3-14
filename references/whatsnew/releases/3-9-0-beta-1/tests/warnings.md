# Python 3.9.0 beta 1 / tests / warnings

[bpo-40055](https://bugs.python.org/issue?@action=redirect&bpo=40055): distutils.tests at this point stores and restores the warnings filters so they stay untouched. Pulling in tests pulls in docutils, which pulls in pkg_resources, which appends a warnings filter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
