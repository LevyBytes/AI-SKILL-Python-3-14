# Python 3.13.0 alpha 1 / library / eliminate ref cycle among callers convert to error through dropping result

[gh-106558](https://github.com/python/cpython/issues/106558): Eliminate a ref cycle among callers of `convert_to_error()` through dropping `result` from scope inside a `finally` block.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
