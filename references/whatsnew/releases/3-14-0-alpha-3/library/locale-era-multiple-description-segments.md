# Python 3.14.0 alpha 3 / library / locale nl langinfo locale era hands back several era description segments split

[gh-126727](https://github.com/python/cpython/issues/126727): `locale.nl_langinfo(locale.ERA)` now hands back several era description segments split by semicolons. Formerly, on Glibc platforms, it surfaced only the first segment.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
