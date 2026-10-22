# Python 3.8.0 beta 1 / library / unittest mock

[bpo-31855](https://bugs.python.org/issue?@action=redirect&bpo=31855): Output from [`unittest.mock.mock_open()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.mock_open) now honors the read([size]) argument. Rémi Lapeyre contributed this patch.

[bpo-37047](https://bugs.python.org/issue?@action=redirect&bpo=37047): Manages late binding plus attribute access in [`unittest.mock.AsyncMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.AsyncMock) setup during autospeccing. Records the freshly implemented async methods in [`unittest.mock.MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock).

[bpo-36996](https://bugs.python.org/issue?@action=redirect&bpo=36996): Copes with [`unittest.mock.patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) applied as a decorator over async functions.

[bpo-32299](https://bugs.python.org/issue?@action=redirect&bpo=32299): Adjusted [`unittest.mock.patch.dict()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.dict) so that it hands back the patched dictionary while serving as a context manager. Vadim Tsander supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
