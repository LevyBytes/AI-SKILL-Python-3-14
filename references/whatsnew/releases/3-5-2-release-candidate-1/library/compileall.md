# Python 3.5.2 release candidate 1 / library / compileall

[bpo-24903](https://bugs.python.org/issue?@action=redirect&bpo=24903): Correct a regression in how many arguments compileall accepts when "-d" is supplied. The argument-count check was removed entirely, given that it never operated correctly to begin with.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
