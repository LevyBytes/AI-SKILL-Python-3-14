# Python 3.14.6 final / core and builtins / imports and modules

[gh-150146](https://github.com/python/cpython/issues/150146): Repair a segfault on an intricate type variable substitution.

`from typing import TypeVar; memoryview[TypeVar("")][*typing.Mapping[..., ...]]` previously broke owing to a missing `NULL` check inside the `_unpack_args` C function call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
