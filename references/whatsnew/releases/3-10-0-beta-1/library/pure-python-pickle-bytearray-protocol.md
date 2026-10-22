# Python 3.10.0 beta 1 / library / resolved defect pure python pickle code surfaced protocol where bytearray

[bpo-43907](https://bugs.python.org/issue?@action=redirect&bpo=43907): Resolved a defect in the pure-Python pickle code that surfaced with protocol 5, where bytearray instances appearing more than once across the pickled object graph were wrongly unpickled into separate duplicate copies of the bytearray object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
