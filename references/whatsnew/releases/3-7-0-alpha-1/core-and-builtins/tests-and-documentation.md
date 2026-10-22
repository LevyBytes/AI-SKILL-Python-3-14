# Python 3.7.0 alpha 1 / core and builtins / tests and documentation

[bpo-28782](https://bugs.python.org/issue?@action=redirect&bpo=28782): Correct a defect in how `yield from` is implemented when it tests whether the following instruction is YIELD_FROM. This was a regression that WORDCODE introduced ([bpo-26647](https://bugs.python.org/issue?@action=redirect&bpo=26647)).

[bpo-28379](https://bugs.python.org/issue?@action=redirect&bpo=28379): Added sanity checks plus tests covering PyUnicode_CopyCharacters(). Xiang Zhang wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
