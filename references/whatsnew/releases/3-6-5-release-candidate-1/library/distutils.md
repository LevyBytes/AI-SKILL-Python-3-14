# Python 3.6.5 release candidate 1 / library / distutils

[bpo-32304](https://bugs.python.org/issue?@action=redirect&bpo=32304): The distutils’ upload command will no longer damage tar files that end in a CR byte, nor will it attempt CR to CRLF conversion inside any of the upload text fields.

[bpo-32302](https://bugs.python.org/issue?@action=redirect&bpo=32302): Repair distutils’ bdist_wininst for CRT v142: it is binary compatible with CRT v140.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
