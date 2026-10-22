# Python 3.11.0 alpha 2 / tests / resource

[bpo-43592](https://bugs.python.org/issue?@action=redirect&bpo=43592): `test.libregrtest` will now bump the soft resource ceiling on open file descriptors whenever the platform default falls short of what our test suite needs, a situation common on macOS.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
