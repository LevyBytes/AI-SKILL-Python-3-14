# Python 3.13.0 alpha 1 / library / unittest mock

[gh-94924](https://github.com/python/cpython/issues/94924): [`unittest.mock.create_autospec()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.create_autospec) now correctly yields coroutine functions that work with [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction)

[bpo-44185](https://bugs.python.org/issue?@action=redirect&bpo=44185): [`unittest.mock.mock_open()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.mock_open) now invokes the file handle mock's `close()` method as it leaves the context manager. Samet Yaslan authored the patch.

[bpo-41768](https://bugs.python.org/issue?@action=redirect&bpo=41768): [`unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html#module-unittest.mock) speccing no longer triggers class properties. Melanie Witt authored the patch.

[bpo-17013](https://bugs.python.org/issue?@action=redirect&bpo=17013): Brought `ThreadingMock` to [`unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html#module-unittest.mock), usable for building Mock objects that block until they get called. Karthikeyan Singaravelan and Mario Corchero authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
