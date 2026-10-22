# Python 3.8.0 alpha 1 / tests / imports and modules

[bpo-32872](https://bugs.python.org/issue?@action=redirect&bpo=32872): Sidestep a regrtest incompatibility tied to namespace packages.

[bpo-34200](https://bugs.python.org/issue?@action=redirect&bpo=34200): Removed the non-deterministic flakiness in test_pkg by avoiding the scary test.support.module_cleanup() logic that saves and restores the contents of sys.modules across test cases.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
