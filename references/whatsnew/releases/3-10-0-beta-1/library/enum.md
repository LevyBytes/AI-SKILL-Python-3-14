# Python 3.10.0 beta 1 / library / enum

[bpo-43957](https://bugs.python.org/issue?@action=redirect&bpo=43957): [Enum] The `TypeError` thrown when a non-member appears in a containment check is now deprecated; starting in 3.12 the check will instead yield `True` or `False`, returning `True` when the value is a member of that enum or matches one of its members? value.

[bpo-43945](https://bugs.python.org/issue?@action=redirect&bpo=43945): [Enum] The non-standard mixin format() behavior is deprecated: from 3.12 onward format() calls will operate on the enum member rather than on the member's value.

[bpo-43744](https://bugs.python.org/issue?@action=redirect&bpo=43744): correct a problem in which an enum member name lines up with the beginning of a private variable name

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
