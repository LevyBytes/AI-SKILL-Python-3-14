# Python 3.5.3 release candidate 1 / core and builtins / functions and types

[bpo-28991](https://bugs.python.org/issue?@action=redirect&bpo=28991): functools.lru_cache() carried an obscure reentrancy bug that a monkey-patched len() function could trigger.

[bpo-26906](https://bugs.python.org/issue?@action=redirect&bpo=26906): Looking up special methods on an uninitialized type now triggers implicit initialization of that type instead of failing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
