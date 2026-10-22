# Python 3.10.0 beta 1 / library / importlib metadata

[bpo-43926](https://bugs.python.org/issue?@action=redirect&bpo=43926): Inside `importlib.metadata`, offer one consistent interface to `Description`, permit every field to carry multiline values, strip continuation lines out of multiline values, and supply a `.json` property granting ready access to the PEP 566 JSON-compatible form. Sync with `importlib_metadata 4.0`.

[bpo-43780](https://bugs.python.org/issue?@action=redirect&bpo=43780): Within `importlib.metadata`, pull in changes from importlib_metadata 3.10: introduce mtime-based caching while distributions are discovered. Marked the dict result coming from `entry_points()` as deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
