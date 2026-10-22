# Python 3.7.0 beta 1 / library / locale

[bpo-31900](https://bugs.python.org/issue?@action=redirect&bpo=31900): To decode the `decimal_point` and `thousands_sep` byte strings when they are non-ASCII or run beyond 1 byte, and whenever the `LC_NUMERIC` locale differs from the `LC_CTYPE` locale, the [`locale.localeconv()`](https://docs.python.org/3.14/library/locale.html#locale.localeconv) function now briefly switches the `LC_CTYPE` locale over to the `LC_NUMERIC` locale. Other threads feel this momentary change. The [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method gets the identical treatment when it formats a number ([`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), `float` and subclasses) using the `n` type (ex: `'{:n}'.format(1234)`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
