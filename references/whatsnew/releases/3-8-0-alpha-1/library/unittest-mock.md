# Python 3.8.0 alpha 1 / library / unittest mock

[bpo-33516](https://bugs.python.org/issue?@action=redirect&bpo=33516): [`unittest.mock.MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock) gained support for the `__round__` magic method.

[bpo-32933](https://bugs.python.org/issue?@action=redirect&bpo=32933): [`unittest.mock.mock_open()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.mock_open) now permits iteration across the file contents. Patch by Tony Flury.

[bpo-31177](https://bugs.python.org/issue?@action=redirect&bpo=31177): Fixed a defect that blocked calling [`reset_mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.reset_mock) on mock instances whose attributes had been deleted

[bpo-20239](https://bugs.python.org/issue?@action=redirect&bpo=20239): Permit repeated assignment and deletion of [`unittest.mock.Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) attributes. Patch by Pablo Galindo.

[bpo-35226](https://bugs.python.org/issue?@action=redirect&bpo=35226): Walk arguments recursively when checking [`unittest.mock.call`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.call) objects for equality, and note that following the parameters used to build ancestors of mocks inside `mock_calls` cannot be done.

[bpo-35047](https://bugs.python.org/issue?@action=redirect&bpo=35047): `unittest.mock` now folds the mock calls into its exception messages whenever `assert_not_called`, `assert_called_once`, or `assert_called_once_with` fails. Patch by Petter Strandmark.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
