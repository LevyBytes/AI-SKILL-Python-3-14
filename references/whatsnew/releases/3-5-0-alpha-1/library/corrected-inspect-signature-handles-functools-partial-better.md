# Python 3.5.0 alpha 1 / library / corrected inspect signature handles functools partial better

[bpo-21117](https://bugs.python.org/issue?@action=redirect&bpo=21117): Corrected inspect.signature so it handles functools.partial better. Because of how functools.partial is implemented, positional-or-keyword arguments handed in as keyword arguments turn into keyword-only.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
