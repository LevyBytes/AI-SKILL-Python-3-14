# Python 3.13.0 alpha 1 / tests / debug

[gh-109276](https://github.com/python/cpython/issues/109276): libregrtest now relies on a dedicated file descriptor for emitting the test result as JSON. Previously, should a test emit debug messages right around the JSON, the main test process could not parse the JSON. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
