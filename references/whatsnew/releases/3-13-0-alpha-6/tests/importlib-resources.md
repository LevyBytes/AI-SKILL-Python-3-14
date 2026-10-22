# Python 3.13.0 alpha 6 / tests / importlib resources

[gh-116307](https://github.com/python/cpython/issues/116307): Introduced the import helper `isolated_modules`, because `CleanImport` leaves behind modules brought in during the context. Apply it across the importlib.resources tests so `mod` is not left lingering to trip up the importlib.metadata tests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
