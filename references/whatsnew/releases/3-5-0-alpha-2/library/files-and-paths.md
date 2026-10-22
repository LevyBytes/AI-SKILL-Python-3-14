# Python 3.5.0 alpha 2 / library / files and paths

[bpo-5700](https://bugs.python.org/issue?@action=redirect&bpo=5700): io.FileIO() ran flush() once the file was already closed. With closefd=False, close() skipped the flush() call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
