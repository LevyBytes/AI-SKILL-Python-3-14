# Python 3.5.0 alpha 3 / library / within bufferedrwpair close reader bufferedrwpair shut even after closing writer

[bpo-21802](https://bugs.python.org/issue?@action=redirect&bpo=21802): Within BufferedRWPair.close(), the reader in BufferedRWPair is now shut even after closing the writer fails.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
