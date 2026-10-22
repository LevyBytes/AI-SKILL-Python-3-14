# Python 3.14.2 final / library / functions and types

[gh-140797](https://github.com/python/cpython/issues/140797): Roll back the changes to the undocumented `re.Scanner` class. Capturing groups stay permitted for backward compatibility, even though relying on them may yield an incorrect result. A later Python version will disallow them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
