# Python 3.7.0 beta 5 / library / dataclasses

[bpo-33453](https://bugs.python.org/issue?@action=redirect&bpo=33453): Repair dataclasses so they function with literal string type annotations or with PEP 563 style "Postponed Evaluation of Annotations". Detection is limited to particular string prefixes for ClassVar ("ClassVar" and "typing.ClassVar") along with InitVar ("InitVar" and "dataclasses.InitVar").

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
