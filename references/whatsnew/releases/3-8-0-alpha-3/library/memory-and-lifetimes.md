# Python 3.8.0 alpha 3 / library / memory and lifetimes

[bpo-36179](https://bugs.python.org/issue?@action=redirect&bpo=36179): Close two improbable reference leaks within _hashopenssl. Those leaks only show up in out-of-memory situations.

[bpo-35715](https://bugs.python.org/issue?@action=redirect&bpo=35715): Frees a ProcessPoolExecutor _process_worker's return value once it is no longer required, reclaiming memory

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
