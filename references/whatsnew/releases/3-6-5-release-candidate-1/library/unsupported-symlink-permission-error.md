# Python 3.6.5 release candidate 1 / library / platforms lacking support chmod follow symlinks false raise notimplementederror rather

[bpo-32277](https://bugs.python.org/issue?@action=redirect&bpo=32277): On platforms lacking support for `chmod(..., follow_symlinks=False)`, raise `NotImplementedError` rather than `SystemError`. Anthony Sottile wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
