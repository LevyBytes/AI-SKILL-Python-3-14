# Python 3.10.0 beta 1 / library / functions

[bpo-43478](https://bugs.python.org/issue?@action=redirect&bpo=43478): A Mock can no longer serve as the spec for another Mock. Because of that, an object that is already mocked cannot have one of its attributes mocked through `autospec=True`, nor can it be passed to a `create_autospec(...)` call. Doing so may surface bugs in tests, since these Mock-derived Mocks will always clear certain checks (such as [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance)) and builtin assert functions (for example assert_called_once_with) will pass no matter what.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
