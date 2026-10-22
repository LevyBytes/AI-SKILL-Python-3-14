# Python 3.11.0 alpha 1 / tests / tests and documentation

[bpo-45185](https://bugs.python.org/issue?@action=redirect&bpo=45185): Turns on the `TestEnumerations` test cases inside the `test_ssl` suite.

[bpo-45125](https://bugs.python.org/issue?@action=redirect&bpo=45125): Strengthens the pickling tests and documentation for `SharedMemory` and `SharableList` objects.

[bpo-45042](https://bugs.python.org/issue?@action=redirect&bpo=45042): Resolves a situation where test classes carrying the `@hashlib_helper.requires_hashdigest` decorator were always being skipped.

[bpo-44852](https://bugs.python.org/issue?@action=redirect&bpo=44852): Provide a means to silence DeprecationWarnings wholesale during runs of the regression test suite.

[bpo-44451](https://bugs.python.org/issue?@action=redirect&bpo=44451): Clear `DeprecationWarning` filters within `test.test_importlib.test_metadata_api.APITests.test_entry_points_by_index` so that a `StopIteration` error is not raised whenever `DeprecationWarnings` happen to be suppressed.

[bpo-42083](https://bugs.python.org/issue?@action=redirect&bpo=42083): Provide a test confirming that `PyStructSequence_NewType` will accept a `PyStructSequence_Desc` whose `doc` field is assigned `NULL`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
