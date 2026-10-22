# Python 3.6.5 release candidate 1 / library / locale

[bpo-32555](https://bugs.python.org/issue?@action=redirect&bpo=32555): Under FreeBSD and Solaris, os.strerror() will now always decode the byte string using the current locale encoding instead of falling back to ASCII/surrogateescape in certain situations.

[bpo-31900](https://bugs.python.org/issue?@action=redirect&bpo=31900): The [`locale.localeconv()`](https://docs.python.org/3.14/library/locale.html#locale.localeconv) routine now temporarily switches the `LC_CTYPE` locale to match the `LC_NUMERIC` locale in order to decode the `decimal_point` and `thousands_sep` byte strings whenever they run longer than 1 byte or contain non-ASCII data and the `LC_NUMERIC` locale differs from the `LC_CTYPE` locale. Other threads feel this temporary swap. The identical behavior also applies to the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method while formatting a number ([`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), `float` and subclasses) using the `n` type (ex: `'{:n}'.format(1234)`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
