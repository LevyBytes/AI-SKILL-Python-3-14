# What's New In Python 3.6 / unittest.mock — unittest.mock

### unittest.mock

The following enhancements landed for the [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) class:

- A pair of new methods, [`Mock.assert_called()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called) and [`Mock.assert_called_once()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_once), let you verify that the mock object was invoked. (Contributed by Amit Saha in [bpo-26323](https://bugs.python.org/issue?@action=redirect&bpo=26323).)

- There are now two optional keyword-only parameters on the [`Mock.reset_mock()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.reset_mock) method: *return_value* and *side_effect*. (Contributed by Kushal Das in [bpo-21271](https://bugs.python.org/issue?@action=redirect&bpo=21271).)

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](urllib-request.md) · [Release/subject declaration](summary-release-highlights.md)
