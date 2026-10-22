# Python 3.8.0 alpha 1 / library / fnmatch

[bpo-32775](https://bugs.python.org/issue?@action=redirect&bpo=32775): [`fnmatch.translate()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.translate) no longer generates patterns carrying set operations. Sets that open with "[" or hold `--`, "&&", "~~" or "||" are slated for a different interpretation inside regular expressions down the line. For now they raise warnings. fnmatch.translate() will now steer clear of accidentally emitting patterns that hold such sets.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
