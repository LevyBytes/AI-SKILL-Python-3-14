# Python 3.7.0 alpha 1 / library / tests and documentation

[bpo-30298](https://bugs.python.org/issue?@action=redirect&bpo=30298): The deprecation-warning condition for inline modifiers was relaxed. Several consecutive inline modifiers may now appear at the pattern's start (for example `'(?i)(?s)...'`). Under verbose mode, whitespace and comments are now accepted both before and between inline modifiers (for example `'(?x) (?i) (?s)...'`).

[bpo-26915](https://bugs.python.org/issue?@action=redirect&bpo=26915): The index() and count() methods on collections.abc.Sequence now test identity ahead of equality while doing comparisons.

[bpo-28624](https://bugs.python.org/issue?@action=redirect&bpo=28624): A test was added confirming the cwd parameter of Popen() takes PathLike objects. Sayan Chowdhury provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
