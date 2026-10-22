# Python 3.9.0 alpha 4 / library / unittest mock

[bpo-39485](https://bugs.python.org/issue?@action=redirect&bpo=39485): Fix a bug in [`unittest.mock.create_autospec()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.create_autospec) that complained about an incorrect argument count for custom descriptors which an extension module defines to return functions.

[bpo-25597](https://bugs.python.org/issue?@action=redirect&bpo=25597): Make sure that, when `wraps` is handed to [`unittest.mock.MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock), it drives the computation of return values for the magic methods rather than falling back on the default return values. Karthikeyan Singaravelan authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
