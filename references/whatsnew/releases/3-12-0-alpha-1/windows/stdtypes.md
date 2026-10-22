# Python 3.12.0 alpha 1 / windows / stdtypes

[bpo-42658](https://bugs.python.org/issue?@action=redirect&bpo=42658): Enable native, case-insensitive Windows path comparisons by having `ntpath.normcase()` call `LCMapStringEx` rather than [`str.lower()`](https://docs.python.org/3.14/library/stdtypes.html#str.lower). The `_winapi` module gains `LCMapStringEx`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
