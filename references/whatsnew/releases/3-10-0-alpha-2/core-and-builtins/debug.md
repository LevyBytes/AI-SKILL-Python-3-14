# Python 3.10.0 alpha 2 / core and builtins / debug

[bpo-42218](https://bugs.python.org/issue?@action=redirect&bpo=42218): Squashed a PEG parser bug that triggered crashes under debug mode. Errors are checked within left-recursive rules now, sidestepping situations where those errors go unhandled in time and surface as far-off crashes elsewhere.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
