# Python 3.5.1 release candidate 1 / core and builtins / functions and types

[bpo-22995](https://bugs.python.org/issue?@action=redirect&bpo=22995): The default __reduce__ and __reduce_ex__ implementations now turn away builtin types whose __new__ is not defined.

[bpo-24726](https://bugs.python.org/issue?@action=redirect&bpo=24726): Corrected both a crash and a leaking NULL within repr() of an OrderedDict that had been mutated through direct calls of dict methods.

[bpo-24806](https://bugs.python.org/issue?@action=redirect&bpo=24806): Kept builtin types that may not be subclassed from being subclassed by way of multiple inheritance.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
