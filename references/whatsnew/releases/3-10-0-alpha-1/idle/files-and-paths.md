# Python 3.10.0 alpha 1 / idle / files and paths

[bpo-41373](https://bugs.python.org/issue?@action=redirect&bpo=41373): Files opened with no line ending — for instance when empty — or with mixed line endings are now saved using the system default line ending. This addresses a regression from 3.8.4 and 3.9.0b4.

[bpo-41300](https://bugs.python.org/issue?@action=redirect&bpo=41300): Allow saving files that contain non-ascii chars. Addresses a regression shipped in 3.9.0b4 and 3.8.4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
