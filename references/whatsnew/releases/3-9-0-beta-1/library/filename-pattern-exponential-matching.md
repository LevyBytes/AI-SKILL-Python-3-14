# Python 3.9.0 beta 1 / library / where several pattern characters appeared fnmatch fnmatch could run exponential

[bpo-40480](https://bugs.python.org/issue?@action=redirect&bpo=40480): Where several `*` pattern characters appeared, `fnmatch.fnmatch()` could run in exponential time. The fix builds more intricate regular expressions that sidestep pointless backtracking.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
