# locale: `locale.getdefaultlocale()`, `locale.getlocale()`, `locale.getpreferredencoding()`, `locale.getencoding()`, `locale.normalize()`, `locale.strcoll()`, `locale.strxfrm()`, `locale.format_string()`, `locale.currency()`

locale.getdefaultlocale([*envvars*])

Tries to work out the default locale settings, handing them back as a tuple shaped like `(language code, encoding)`.

By the POSIX definition, a program that has not called `setlocale(LC_ALL, '')` runs under the portable `'C'` locale. Calling `setlocale(LC_ALL, '')` lets it adopt the default locale as the `LANG` variable defines it. Because we have no wish to disturb the current locale setting, we therefore emulate the behavior outlined above.

For the sake of compatibility with other platforms, the test covers not only the `LANG` variable but a list of variables handed in via the envvars parameter. Whichever turns out to be defined first gets used. *envvars* defaults to the search path that GNU gettext uses; it must always include the variable name `'LANG'`. The GNU gettext search path holds `'LC_ALL'`, `'LC_CTYPE'`, `'LANG'` and `'LANGUAGE'`, in that order.

The language code carries the same format as a locale name, only without encoding and `@`-modifier. The language code and encoding may be `None` whenever their values cannot be worked out. As `(None, None)` the "C" locale is represented.

 locale.getlocale(*category=LC_CTYPE*)

Returns the current setting for the given locale category as a tuple holding the language code and encoding. *category* may be one of the `LC_*` values apart from `LC_ALL`. Its default is `LC_CTYPE`.

The language code carries the same format as a locale name, only without encoding and `@`-modifier. The language code and encoding may be `None` whenever their values cannot be worked out. As `(None, None)` the "C" locale is represented.

 locale.getpreferredencoding(*do_setlocale=True*)

Return the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding) used for text data, as user preferences dictate. User preferences take different forms across different systems, and on certain systems may be unavailable programmatically, so this function only returns a guess.

On certain systems, calling `setlocale()` is required to obtain the user preferences, hence this function is not thread-safe. Where calling setlocale is neither required nor wanted, *do_setlocale* should be set to `False`.

On Android, or where the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) is enabled, always return `'utf-8'`; the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding) and the *do_setlocale* argument are disregarded.

The [Python preinitialization](https://docs.python.org/3.14/c-api/init_config.html#c-preinit) configures the LC_CTYPE locale. See also the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

Changed in version 3.7: On Android, or where the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) is enabled, the function now always returns `"utf-8"`.

 locale.getencoding()

Get the current [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding):

- On Android and VxWorks, return `"utf-8"`.

- On Unix, return the encoding of the current `LC_CTYPE` locale. Return `"utf-8"` when `nl_langinfo(CODESET)` returns an empty string: for example, when the current LC_CTYPE locale goes unsupported.

- On Windows, return the ANSI code page.

The [Python preinitialization](https://docs.python.org/3.14/c-api/init_config.html#c-preinit) configures the LC_CTYPE locale. See also the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

This function resembles `getpreferredencoding(False)`, except that this one disregards the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode).

Added in version 3.11.

 locale.normalize(*localename*)

Returns a normalized locale code for the given locale name. The locale code that comes back is formatted for use with `setlocale()`. Should normalization fail, the original name comes back unchanged.

Should the given encoding be unknown, the function falls back on the default encoding for the locale code, exactly as `setlocale()` does.

 locale.strcoll(*string1*, *string2*)

Compares two strings per the current `LC_COLLATE` setting. Like any other compare function, it returns a negative value, a positive value, or `0`, according to whether *string1* collates ahead of *string2*, after it, or equal to it.

 locale.strxfrm(*string*)

Transforms a string into one usable in locale-aware comparisons. As an example, `strxfrm(s1) < strxfrm(s2)` is equivalent to `strcoll(s1, s2) < 0`. You can reach for this function when the same string is compared over and over, e.g. while collating a sequence of strings.

 locale.format_string(*format*, *val*, *grouping=False*, *monetary=False*)

Formats a number *val* per the current `LC_NUMERIC` setting. The format keeps to whatever conventions the `%` operator follows. For floating-point values, where appropriate the decimal point is adjusted. When *grouping* is `True`, the grouping is taken into account as well.

When *monetary* is true, the conversion applies the monetary thousands separator and grouping strings.

Processes formatting specifiers as in `format % val`, while taking the current locale settings into account.

Changed in version 3.7: The *monetary* keyword parameter was added.

 locale.currency(*val*, *symbol=True*, *grouping=False*, *international=False*)

Formats a number *val* per the current `LC_MONETARY` settings.

The string that comes back carries the currency symbol when *symbol* is true, which is the default. When *grouping* is `True` (which is not the default), grouping is applied to the value. When *international* is `True` (not the default), the symbol used is the international currency symbol.

Note

With the "C" locale this function will not work, so a locale has to be set first by way of `setlocale()`.

[Subject index](INDEX.md) · [Previous](locale-abmon-1-to-locale-alt-digits.md) · [Continue](locale-str-to-locale-char-max.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
