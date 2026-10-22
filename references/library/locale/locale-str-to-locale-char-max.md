# locale: Localized number conversion and locale category constants

locale.str(*float*)

Formats a floating-point number with the same format that the built-in function `str(float)` uses, yet honoring the decimal point.

 locale.delocalize(*string*)

Converts a string into a normalized number string, following the `LC_NUMERIC` settings.

Added in version 3.5.

 locale.localize(*string*, *grouping=False*, *monetary=False*)

Converts a normalized number string into a formatted string following the `LC_NUMERIC` settings.

Added in version 3.10.

 locale.atof(*string*, *func=float*)

Converts a string into a number, honoring the `LC_NUMERIC` settings, by applying *func* to whatever `delocalize()` returns for *string*.

 locale.atoi(*string*)

Converts a string to an integer, following the `LC_NUMERIC` conventions.

 locale.LC_CTYPE

Locale category for the character type functions. Most crucially, this category sets the text encoding, that is, how bytes get interpreted as Unicode codepoints. Consult [**PEP 538**](https://peps.python.org/pep-0538/) and [**PEP 540**](https://peps.python.org/pep-0540/) for how this variable might be coerced automatically to `C.UTF-8` so as to dodge problems caused by invalid settings inside containers or by incompatible settings handed over remote SSH connections.

Python does not internally use locale-dependent character transformation functions from `ctype.h`. In their place, `pyctype.h` supplies locale-independent equivalents such as [`Py_TOLOWER`](https://docs.python.org/3.14/c-api/conversion.html#c.Py_TOLOWER).

 locale.LC_COLLATE

Locale category for sorting strings. The `locale` module's `strcoll()` and `strxfrm()` functions are the ones affected.

 locale.LC_TIME

Locale category for the formatting of time. These conventions are what the [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) function follows.

 locale.LC_MONETARY

Locale category for formatting of monetary values. The `localeconv()` function makes the available options available.

 locale.LC_MESSAGES

Locale category for message display. At present Python provides no support for application specific locale-aware messages. Messages that the operating system displays, like those [`os.strerror()`](https://docs.python.org/3.14/library/os.html#os.strerror) returns, might be affected by this category.

On operating systems that do not conform to the POSIX standard, most notably Windows, this value may be unavailable.

 locale.LC_NUMERIC

Locale category for formatting numbers. That category affects the `locale` module's `format_string()`, `atoi()`, `atof()` and `str()` functions. Every other numeric formatting operation is left unaffected.

 locale.LC_ALL

Combination of all locale settings. Where this flag is used while the locale is changed, setting the locale across all categories is attempted. Should that fail for any one category, then no category is changed whatsoever. Where the locale is retrieved by means of this flag, a string indicating the setting across all categories is returned. That string can be used later to restore the settings.

 locale.CHAR_MAX

This is a symbolic constant used for different values returned by `localeconv()`.

[Subject index](INDEX.md) · [Previous](locale-getdefaultlocale-to-locale-currency.md) · [Continue](background-details-hints-tips-and-caveats.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
