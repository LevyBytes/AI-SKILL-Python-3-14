# Python 3.11.0 alpha 3 / core and builtins / memory and lifetimes

[bpo-45947](https://bugs.python.org/issue?@action=redirect&bpo=45947): Position the pointers for dict and values right ahead of the GC header. As a result, the count of dependent memory loads required to reach either dict or values drops from 3 down to 1.

[bpo-42268](https://bugs.python.org/issue?@action=redirect&bpo=42268): When the chosen compiler lacks memory sanitizer support, the configure step now fails. The patch came from Pablo Galindo

[bpo-45786](https://bugs.python.org/issue?@action=redirect&bpo=45786): Reserve room for the interpreter frame within the frame object itself, sidestepping a second allocation whenever the frame object survives past the frame activation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
