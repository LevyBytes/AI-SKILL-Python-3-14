# locale: `locale.Error`, `locale.setlocale()`

### `locale` - Internationalization services

**Source code:** [Lib/locale.py](https://github.com/python/cpython/tree/3.14/Lib/locale.py)

---

Access to the POSIX locale database and its functionality is opened up by the `locale` module. The POSIX locale mechanism lets programmers handle certain cultural matters within an application, without the programmer having to know every specific of each country where the software runs.

The `locale` module is built atop the `_locale` module, which in turn draws on an ANSI C locale implementation where one is available.

The exception and functions below are defined by the `locale` module:

 *exception *locale.Error

Exception raised when the locale passed to `setlocale()` is not recognized.

 locale.setlocale(*category*, *locale=None*)

When *locale* is supplied and not `None`, `setlocale()` changes the locale setting for the *category*. The data description further down lists the available categories. *locale* may be a string, or else a pair of language code and encoding. The user's default settings are denoted by an empty string. Where changing the locale fails, the exception `Error` is raised. On success, the new locale setting is returned.

When *locale* is a pair, the locale aliasing engine converts it into a locale name. The language code carries the same format as a locale name, only without encoding and `@`-modifier. Both the language code and the encoding can be `None`.

When *locale* is left out or `None`, the current setting for *category* is returned.

Example:

```python
>>> import locale
>>> loc = locale.setlocale(locale.LC_ALL)  # get current locale
# use German locale; name and availability varies with platform
>>> locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
>>> locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut
>>> locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
>>> locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale
>>> locale.setlocale(locale.LC_ALL, loc)  # restore saved locale

```

On most systems `setlocale()` is not thread-safe. As a rule applications open with a call of:

```python
import locale
locale.setlocale(locale.LC_ALL, '')

```

That sets the locale across all categories to the user's default setting (usually named in the `LANG` environment variable). Provided the locale stays unchanged afterward, using multithreading ought not cause trouble.

[Subject index](INDEX.md) · [Continue](locale-localeconv-to-locale-t-fmt-ampm.md)
