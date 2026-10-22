# Python 3.12.0 alpha 1 / library / importlib metadata

[gh-97781](https://github.com/python/cpython/issues/97781): Dropped deprecated interfaces from `importlib.metadata` (entry points reached as a dictionary, implicit dictionary construction out of a sequence of `EntryPoint` objects, mutability of the `EntryPoints` result, indexing into an entry point). `entry_points` now exposes a cleaner, more direct API (it returns `EntryPoints`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
