# Python 3.14.6 final / library / unittest mock

[gh-150175](https://github.com/python/cpython/issues/150175): Repair a race condition within [`unittest.mock.ThreadingMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.ThreadingMock) where simultaneous calls could drop increments to `call_count` plus other attributes owing to a missing lock inside `_increment_mock_call`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
