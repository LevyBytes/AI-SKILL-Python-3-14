# Python 3.7.0 beta 2 / library / fnmatch

[bpo-32775](https://bugs.python.org/issue?@action=redirect&bpo=32775): [`fnmatch.translate()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.translate) no longer emits patterns that hold set operations. Sets that begin with "[" or that contain `--`, "&&", "~~" or "||" are going to be read differently within regular expressions in upcoming versions. For now they raise warnings. fnmatch.translate() now keeps from accidentally emitting patterns that carry such sets.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
