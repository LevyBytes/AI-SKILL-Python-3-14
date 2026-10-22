# Python 3.11.0 alpha 6 / c api / python s public headers stop importing stdbool h code embedding

[bpo-46748](https://bugs.python.org/issue?@action=redirect&bpo=46748): Python's public headers stop importing `<stdbool.h>`, so code embedding or extending Python is free to define `bool`, `true` and `false` itself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
