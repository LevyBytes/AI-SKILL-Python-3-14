# Python 3.14.0 alpha 5 / library / gettext

[gh-118761](https://github.com/python/cpython/issues/118761): Make importing [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) as much as ten times cheaper by loading [`re`](https://docs.python.org/3.14/library/re.html#module-re) only when needed. As a result, `re` is no longer implicitly exposed as `gettext.re`. Eli Schwartz contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
