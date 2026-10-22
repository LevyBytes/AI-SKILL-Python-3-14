# Python 3.14.6 final / library / json

[gh-142831](https://github.com/python/cpython/issues/142831): Repair a segfault within the [`json`](https://docs.python.org/3.14/library/json.html#module-json) module where a use-after-free might arise should the object under encoding get modified mid-serialization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
