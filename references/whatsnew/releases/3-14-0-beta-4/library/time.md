# Python 3.14.0 beta 4 / library / time

[gh-136028](https://github.com/python/cpython/issues/136028): In [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime), parsing of month names that include “İ” (U+0130, LATIN CAPITAL LETTER I WITH DOT ABOVE) was fixed. Locales az_AZ, ber_DZ, ber_MA and crh_UA are affected.

[gh-53203](https://github.com/python/cpython/issues/53203): Repair [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) handling the `%c` and `%x` formats under locales byn_ER, wal_ET and lzh_TW, plus the `%X` format under locales ar_SA, bg_BG and lzh_TW.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
