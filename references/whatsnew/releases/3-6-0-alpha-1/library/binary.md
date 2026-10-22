# Python 3.6.0 alpha 1 / library / binary

[bpo-26709](https://bugs.python.org/issue?@action=redirect&bpo=26709): Repaired a Y2038 problem encountered while loading binary PLists.

[bpo-25510](https://bugs.python.org/issue?@action=redirect&bpo=25510): At end of input fileinput.FileInput.readline() now hands back `b''` rather than `''` whenever the FileInput was opened under binary mode. Ryosuke Ito provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
