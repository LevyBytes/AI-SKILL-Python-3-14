# Python 3.9.0 alpha 3 / library / exceptions and tracebacks

[bpo-39191](https://bugs.python.org/issue?@action=redirect&bpo=39191): `loop.run_until_complete()` now checks for an already-running loop before kicking off a new task, failing fast and preventing a new task from being spawned ahead of the exception being raised.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
