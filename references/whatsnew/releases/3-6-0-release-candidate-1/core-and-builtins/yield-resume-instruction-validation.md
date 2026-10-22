# Python 3.6.0 release candidate 1 / core and builtins / repair bug how yield implemented checks whether upcoming instruction

[bpo-28782](https://bugs.python.org/issue?@action=redirect&bpo=28782): Repair a bug in how `yield from` is implemented when it checks whether the upcoming instruction is YIELD_FROM. This regression came from WORDCODE ([bpo-26647](https://bugs.python.org/issue?@action=redirect&bpo=26647)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
