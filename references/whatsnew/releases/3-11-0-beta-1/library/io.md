# Python 3.11.0 beta 1 / library / io

[bpo-26175](https://bugs.python.org/issue?@action=redirect&bpo=26175): Completely satisfy the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) or [`io.TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase) interface where [`tempfile.SpooledTemporaryFile`](https://docs.python.org/3.14/library/tempfile.html#tempfile.SpooledTemporaryFile) objects are concerned. As a result they cooperate properly with higher-level layers such as compression modules. Carey Metcalfe authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
