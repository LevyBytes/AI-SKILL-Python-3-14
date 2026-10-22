# Python 3.9.0 alpha 5 / core and builtins / warnings

[bpo-19466](https://bugs.python.org/issue?@action=redirect&bpo=19466): Wipe the frames of daemon threads sooner while Python is shutting down so object destructors get called. Consequently, ?unclosed file? resource warnings now show up for daemon threads far more dependably.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
