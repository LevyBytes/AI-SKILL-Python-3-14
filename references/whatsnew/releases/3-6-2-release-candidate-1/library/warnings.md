# Python 3.6.2 release candidate 1 / library / warnings

[bpo-30375](https://bugs.python.org/issue?@action=redirect&bpo=30375): Whenever a regular expression is compiled, the warnings raised now consistently reference the line within the user's own code. Formerly, when raised from within conditionals or groups, they might instead reference the re module's internals.

[bpo-30298](https://bugs.python.org/issue?@action=redirect&bpo=30298): Relax how strict deprecation warnings are for inline modifiers. Several consecutive inline modifiers are now permitted at the pattern's beginning (e.g. `'(?i)(?s)...'`). Under verbose mode, whitespace and comments may now appear before and between inline modifiers (e.g. `'(?x) (?i) (?s)...'`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
