# Python 3.10.0 beta 1 / library / corrected handling dataclass deriving frozen field less dataclass

[bpo-43176](https://bugs.python.org/issue?@action=redirect&bpo=43176): Corrected the handling of a dataclass deriving from a frozen, field-less dataclass. Such a case is now properly flagged as an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
