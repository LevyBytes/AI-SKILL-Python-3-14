# Python 3.13.0 alpha 2 / library / numeric behavior

[gh-97928](https://github.com/python/cpython/issues/97928): Alter how `tkinter.Text.count()` behaves. Given one or zero counting options, it now consistently hands back an integer. Earlier it might give a lone count as a 1-tuple, an integer (solely when the `"update"` option was provided), or `None` where nothing was found. That outcome now holds regardless of whether `wantobjects` equals `0`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
