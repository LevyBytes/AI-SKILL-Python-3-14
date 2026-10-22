# Python 3.5.0 alpha 1 / library / asyncore

[bpo-11453](https://bugs.python.org/issue?@action=redirect&bpo=11453): asyncore: A ResourceWarning is now emitted when an unclosed file_wrapper object gets destroyed. Where necessary the destructor closes the file. Calling close() a second time is now allowed and simply does nothing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
