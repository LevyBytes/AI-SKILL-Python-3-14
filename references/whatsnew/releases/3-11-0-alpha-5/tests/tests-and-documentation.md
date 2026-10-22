# Python 3.11.0 alpha 5 / tests / tests and documentation

[bpo-43478](https://bugs.python.org/issue?@action=redirect&bpo=43478): A Mock can no longer serve as the spec for another Mock. Consequently, an object that is already mocked cannot be handed to `mock.Mock()`. Doing so can mask bugs in tests, because these Mock-derived Mocks always sail through certain checks (such as isinstance) and the builtin assert helpers (such as assert_called_once_with) pass no matter what.

[bpo-46126](https://bugs.python.org/issue?@action=redirect&bpo=46126): Switch off ?descriptions? while tests run internally.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
