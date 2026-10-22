# Python 3.11.0 alpha 1 / library / importlib metadata

[bpo-44464](https://bugs.python.org/issue?@action=redirect&bpo=44464): The flake8 exception in the deprecated importlib.metadata interfaces was removed. Syncs with importlib_metadata 4.6.

[bpo-44246](https://bugs.python.org/issue?@action=redirect&bpo=44246): Within `importlib.metadata`, the output of `Distribution.entry_points` (`EntryPoints`) regained compatibility to meet older-implementation expectations, with deprecation warnings issued for these situations: A. `EntryPoints` objects are mutable again, permitting `sort()` and similar list-style mutation operations. Sidestep the deprecation warnings by converting to a mutable sequence (for example `list(dist.entry_points).sort()`). B. `EntryPoints` results again permit indexed access. Avoid the deprecation warnings by first casting the result into a Sequence (for example `tuple(dist.entry_points)[0]`).

[bpo-44784](https://bugs.python.org/issue?@action=redirect&bpo=44784): Within the importlib.metadata tests, the warnings behavior is now overridden under the expected DeprecationWarnings (importlib_metadata 4.6.3).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
