# Python 3.9.0 alpha 1 / library / fixed dataclasses is dataclass case instance never raises attributeerror inside getattr

[bpo-37868](https://bugs.python.org/issue?@action=redirect&bpo=37868): Fixed dataclasses.is_dataclass for the case of an instance that never raises AttributeError inside __getattr__, that is, an object that hands back something for __dataclass_fields__ even though it is not a dataclass.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
