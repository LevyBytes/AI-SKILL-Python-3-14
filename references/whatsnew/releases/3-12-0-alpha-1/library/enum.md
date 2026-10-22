# Python 3.12.0 alpha 1 / library / enum

[gh-95077](https://github.com/python/cpython/issues/95077): A deprecation warning now fires for enum `member.member` access (for example `Color.RED.BLUE`). The `EnumMeta.__getattr__` hook is removed.

[gh-93910](https://github.com/python/cpython/issues/93910): Reaching the remaining values of an enum through an enum (for instance `Color.RED.BLUE`) is brought back so as to repair a performance regression.

[gh-93820](https://github.com/python/cpython/issues/93820): Pickle [`enum.Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) by name.

[gh-93847](https://github.com/python/cpython/issues/93847): Correct the repr produced for an enum of generic aliases.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
