# Python 3.8.0 alpha 2 / library / unittest mock

[bpo-35512](https://bugs.python.org/issue?@action=redirect&bpo=35512): [`unittest.mock.patch.dict()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.dict), when applied as a decorator together with a string target, now resolves that target as the function runs rather than when the decorator is built. Patch by Karthikeyan Singaravelan.

[bpo-35500](https://bugs.python.org/issue?@action=redirect&bpo=35500): Print the expected versus actual call parameters on distinct lines within [`unittest.mock.Mock.assert_called_with()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_with) assertion errors. Contributed by Susan Su.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
