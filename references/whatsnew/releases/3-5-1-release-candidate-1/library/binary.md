# Python 3.5.1 release candidate 1 / library / binary

[bpo-25510](https://bugs.python.org/issue?@action=redirect&bpo=25510): At end of input, fileinput.FileInput.readline() now hands back `b''` in place of `''` when the FileInput was opened in binary mode. Ryosuke Ito wrote the patch.

[bpo-24881](https://bugs.python.org/issue?@action=redirect&bpo=24881): On Windows and Cygwin the Python FileIO implementation now sets binary mode correctly. Akira Li sent the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
