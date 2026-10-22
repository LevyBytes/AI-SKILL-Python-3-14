# Python 3.6.0 alpha 3 / library / functions and types

[bpo-26721](https://bugs.python.org/issue?@action=redirect&bpo=26721): The socketserver.StreamRequestHandler.wfile attribute was reworked to implement BufferedIOBase. Notably, the write() method has stopped doing partial writes.

[bpo-26243](https://bugs.python.org/issue?@action=redirect&bpo=26243): For zlib.compress(), only the level argument may now be passed by keyword. The first argument has become positional-only.

[bpo-27038](https://bugs.python.org/issue?@action=redirect&bpo=27038): The DirEntry type is now surfaced as os.DirEntry. Jelle Zijlstra contributed the code patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
