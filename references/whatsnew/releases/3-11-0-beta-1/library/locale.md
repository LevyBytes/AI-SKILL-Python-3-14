# Python 3.11.0 beta 1 / library / locale

[gh-91952](https://github.com/python/cpython/issues/91952): Bring `encoding="locale"` support to `TextIOWrapper.reconfigure()`.

[bpo-47000](https://bugs.python.org/issue?@action=redirect&bpo=47000): Have `TextIOWrapper` rely on the locale encoding whenever `encoding="locale"` is given, even while UTF-8 mode is in effect.

[bpo-47000](https://bugs.python.org/issue?@action=redirect&bpo=47000): Provide [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding) for reading the active locale encoding. It behaves much like `locale.getpreferredencoding(False)` while disregarding the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
