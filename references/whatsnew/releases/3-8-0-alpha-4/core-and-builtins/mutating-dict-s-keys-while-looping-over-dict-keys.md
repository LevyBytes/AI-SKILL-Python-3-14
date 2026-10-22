# Python 3.8.0 alpha 4 / core and builtins / mutating dict s keys while looping over dict keys

[bpo-36452](https://bugs.python.org/issue?@action=redirect&bpo=36452): Mutating a `dict`'s keys while looping over the dict, its `keys()`, `values()`, or `items()` is now caught in particular edge cases where additions and removals cancel out so that the key count stays the same. After `len(dict)` iterations the loop raises a `RuntimeError`. Thomas Perl supplied this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
