# Python 3.7.0 alpha 4 / tests / files and paths

[bpo-32252](https://bugs.python.org/issue?@action=redirect&bpo=32252): Repairs faulthandler_suppress_crash_report(), the routine that blocks core dump files while testing crashes. A success from getrlimit() is signalled by a zero return.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
