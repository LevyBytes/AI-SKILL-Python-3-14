# What’s New in Python 2.4 / PEP 331: Locale-Independent Float/String Conversions — locale

### PEP 331: Locale-Independent Float/String Conversions

The [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) modules allow Python programs to pick assorted conversions and display conventions tailored to a given country or language. The module, though, deliberately avoided touching the numeric locale, since several functions inside Python's implementation depended on the numeric locale staying fixed at the `'C'` locale. This was frequently because the code relied on the C library's `atof()` function.

Leaving the numeric locale alone, however, created problems for extensions built on third-party C libraries, since they would lack the proper locale setting. The example that prompted this was GTK+, where the user interface widgets failed to show numbers using the current locale.

The PEP's proposed remedy is to introduce three additional functions into the Python API that carry out ASCII-only conversions while disregarding the locale setting:

- `PyOS_ascii_strtod(str, ptr)` and `PyOS_ascii_atof(str, ptr)` both convert a string to a C double.

- `PyOS_ascii_formatd(buffer, buf_len, format, d)` converts a double to an ASCII string.

These functions' code originated in the GLib library ([https://developer-old.gnome.org/glib/2.26/](http://web.archive.org/web/20210306104320/https://developer.gnome.org/glib/2.26/)), and its developers generously relicensed the pertinent functions and contributed them to the Python Software Foundation. The [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) module is now able to alter the numeric locale, allowing extensions like GTK+ to generate the right output.

See also

[**PEP 331**](https://peps.python.org/pep-0331/) - Locale-Independent Float/String Conversions

Written by Christian R. Reis, and implemented by Gustavo Carneiro.

[Subject index](INDEX.md) · [Previous source section](pep-328-multi-line-imports.md) · [Next source section](core-language-changes.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
