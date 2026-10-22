# Python 3.9.0 alpha 5 / library / unittest mock

[bpo-39915](https://bugs.python.org/issue?@action=redirect&bpo=39915): Make sure that [`unittest.mock.AsyncMock.await_args_list`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list) stores its call objects following the sequence of awaited arguments, rather than relying on [`unittest.mock.Mock.call_args`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.call_args), which only retains the final call's value. Karthikeyan Singaravelan supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
