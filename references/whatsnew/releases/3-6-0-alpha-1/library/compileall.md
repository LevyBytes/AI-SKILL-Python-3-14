# Python 3.6.0 alpha 1 / library / compileall

[bpo-24903](https://bugs.python.org/issue?@action=redirect&bpo=24903): Corrected a regression in how many arguments compileall accepts when "-d" is given. The argument-count check was removed entirely since it never functioned correctly to begin with.

[bpo-25768](https://bugs.python.org/issue?@action=redirect&bpo=25768): The compileall functions now hand back booleans rather than ints, with proper documentation and tests added for those return values.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
