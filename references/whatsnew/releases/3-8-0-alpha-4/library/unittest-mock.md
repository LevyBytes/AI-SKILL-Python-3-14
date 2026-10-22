# Python 3.8.0 alpha 4 / library / unittest mock

[bpo-23078](https://bugs.python.org/issue?@action=redirect&bpo=23078): [`unittest.mock.create_autospec()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.create_autospec) now recognizes [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) and [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod). Felipe Ochoa contributed the initial patch.

[bpo-35082](https://bugs.python.org/issue?@action=redirect&bpo=35082): Calling dir on a [`unittest.mock.Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) no longer surfaces attributes that were deleted.

[bpo-36366](https://bugs.python.org/issue?@action=redirect&bpo=36366): Invoking `stop()` against a [`unittest.mock.patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) object that was never started or already stopped now yields `None` rather than throwing [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError), which renders the method idempotent. Karthikeyan Singaravelan authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
