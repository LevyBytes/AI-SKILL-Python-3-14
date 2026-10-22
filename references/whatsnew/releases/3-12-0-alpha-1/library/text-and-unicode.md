# Python 3.12.0 alpha 1 / library / text and unicode

[gh-91922](https://github.com/python/cpython/issues/91922): Fix the `sqlite.connect()` function plus the `sqlite.Connection` constructor when running under non-UTF-8 locales. They additionally accept bytes paths that the current FS encoding cannot decode.

[gh-93259](https://github.com/python/cpython/issues/93259): A `ValueError` is now raised whenever `None` or an empty string reaches `Distribution.from_name` (along with other callers).

[gh-91810](https://github.com/python/cpython/issues/91810): Hold back the XML declaration for files opened in `ElementTree.write()` when `encoding='unicode'` is paired with `xml_declaration=None`.

[gh-91760](https://github.com/python/cpython/issues/91760): Tighten the rules governing numerical group references and group names inside regular expressions. Only a run of ASCII digits will now serve as a numerical reference. Within bytes patterns and replacement strings, group names are now limited to ASCII letters, digits, and the underscore.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
