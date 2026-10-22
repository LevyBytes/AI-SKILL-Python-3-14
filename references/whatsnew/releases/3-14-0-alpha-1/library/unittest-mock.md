# Python 3.14.0 alpha 1 / library / unittest mock

[gh-123934](https://github.com/python/cpython/issues/123934): Stops [`unittest.mock.MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock) from wiping out the return values of magic methods once `.reset_mock(return_value=True)` has run.

[gh-65454](https://github.com/python/cpython/issues/65454): [`unittest.mock.Mock.attach_mock()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.attach_mock) will no longer cause a `PropertyMock` that is being attached to be called.

[gh-119600](https://github.com/python/cpython/issues/119600): Adjust [`unittest.mock.patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) so it avoids reading the target's attributes whenever `new_callable` has been supplied. Robert Collins authored the patch.

[gh-120732](https://github.com/python/cpython/issues/120732): Correct how the `name` value reaches the [`unittest.mock.Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) object whenever [`unittest.mock.create_autospec()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.create_autospec) is in use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
