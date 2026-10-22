# Python 3.12.0 alpha 1 / library / check inside multiprocessing resource tracker corrected confirms any write pipe stays

[gh-96819](https://github.com/python/cpython/issues/96819): A check inside `multiprocessing.resource_tracker` was corrected so it confirms any write to a pipe stays within `PIPE_BUF` rather than exceeding it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
