# Python 3.5.0 alpha 1 / library / unittest

[bpo-7559](https://bugs.python.org/issue?@action=redirect&bpo=7559): ImportErrors during unittest test loading are now surfaced as import errors carrying their import exception, rather than as attribute errors once the import has already failed.

[bpo-19746](https://bugs.python.org/issue?@action=redirect&bpo=19746): You can now inspect the errors from unittest discovery without running the test suite. The fresh `errors` attribute on `TestLoader` surfaces these non-fatal errors that discovery ran into.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
