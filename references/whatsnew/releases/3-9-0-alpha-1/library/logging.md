# Python 3.9.0 alpha 1 / library / logging

[bpo-38716](https://bugs.python.org/issue?@action=redirect&bpo=38716): logging: convert the RotatingHandler namer and rotator into class-level attributes. That prevents __init__ from resetting them to None whenever a subclass supplies them via eponymous methods.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
