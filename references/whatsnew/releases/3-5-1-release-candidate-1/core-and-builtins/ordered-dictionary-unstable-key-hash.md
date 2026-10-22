# Python 3.5.1 release candidate 1 / core and builtins / iterating ordereddict whose keys carry unstable hash raises keyerror

[bpo-25449](https://bugs.python.org/issue?@action=redirect&bpo=25449): Iterating an OrderedDict whose keys carry an unstable hash now raises KeyError in the C implementations just as it does in the Python implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
