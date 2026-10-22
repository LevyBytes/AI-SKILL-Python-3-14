# Python 3.13.0 alpha 1 / windows / collections and iteration

[gh-103646](https://github.com/python/cpython/issues/103646): When set up via the Microsoft Store, `pip` no longer falls back to per-user installs by default. That said, because the install directory cannot be written, it ought to settle on a per-user install on its own anyway. This should clear up trouble whenever `pip` receives an option clashing with `--user`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
