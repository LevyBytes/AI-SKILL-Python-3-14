# What’s New In Python 3.5 / Deprecated Python modules, functions and methods - asyncio-future, http.cookies, inspect, re, string, unittest

### Deprecated Python modules, functions and methods

Full deprecation has now arrived for the `formatter` module, and its removal remains planned for Python 3.6.

Use of the `asyncio.async()` function is discouraged; prefer [`ensure_future()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.ensure_future) instead.

Historically the `smtpd` module always decoded the DATA section of email messages through the `utf-8` codec. The new *decode_data* keyword on `SMTPServer` now governs that. While `True` is the default value, that default is deprecated. Supply the *decode_data* keyword with a suitable value to keep the deprecation warning away.

It is deprecated to assign values straight into the [`key`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel.key), [`value`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel.value) and [`coded_value`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel.coded_value) of [`http.cookies.Morsel`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel) objects. Reach for the [`set()`](https://docs.python.org/3.14/library/http.cookies.html#http.cookies.Morsel.set) method instead. Beyond that, the undocumented *LegalChars* parameter of `set()` is deprecated, and now gets ignored.

Handing a format string as the keyword argument *format_string* into the [`format()`](https://docs.python.org/3.14/library/string.html#string.Formatter.format) method of the [`string.Formatter`](https://docs.python.org/3.14/library/string.html#string.Formatter) class is now deprecated. (Contributed by Serhiy Storchaka in [bpo-23671](https://bugs.python.org/issue?@action=redirect&bpo=23671).)

Both the `platform.dist()` and `platform.linux_distribution()` functions are now deprecated. Because Linux distributions describe themselves in far too many varied ways, that job is handed off to a package. (Contributed by Vajrasky Kok and Berker Peksag in [bpo-1322](https://bugs.python.org/issue?@action=redirect&bpo=1322).)

The formerly undocumented `from_function` and `from_builtin` methods belonging to [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature) are deprecated. Reach for the new [`Signature.from_callable()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.from_callable) method instead. (Contributed by Yury Selivanov in [bpo-24248](https://bugs.python.org/issue?@action=redirect&bpo=24248).)

Deprecation has hit the `inspect.getargspec()` function, with removal set for Python 3.6. (See [bpo-20438](https://bugs.python.org/issue?@action=redirect&bpo=20438) for details.)

Within [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect), the [`getfullargspec()`](https://docs.python.org/3.14/library/inspect.html#inspect.getfullargspec), [`getcallargs()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcallargs), and `formatargspec()` functions are deprecated, with the [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) API preferred. (Contributed by Yury Selivanov in [bpo-20438](https://bugs.python.org/issue?@action=redirect&bpo=20438).)

The [`getargvalues()`](https://docs.python.org/3.14/library/inspect.html#inspect.getargvalues) and [`formatargvalues()`](https://docs.python.org/3.14/library/inspect.html#inspect.formatargvalues) functions got mistakenly flagged as deprecated when Python 3.5.0 shipped.

It is now deprecated to use the [`re.LOCALE`](https://docs.python.org/3.14/library/re.html#re.LOCALE) flag together with str patterns or to use [`re.ASCII`](https://docs.python.org/3.14/library/re.html#re.ASCII). (Contributed by Serhiy Storchaka in [bpo-22407](https://bugs.python.org/issue?@action=redirect&bpo=22407).)

Employing unrecognized special sequences formed from `'\'` plus an ASCII letter inside regular expression patterns and replacement patterns now triggers a deprecation warning and becomes disallowed in Python 3.6. (Contributed by Serhiy Storchaka in [bpo-23622](https://bugs.python.org/issue?@action=redirect&bpo=23622).)

The undocumented and unofficial *use_load_tests* default argument of the [`unittest.TestLoader.loadTestsFromModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule) method is now deprecated and gets ignored. (Contributed by Robert Collins and Barry A. Warsaw in [bpo-16662](https://bugs.python.org/issue?@action=redirect&bpo=16662).)

[Subject index](INDEX.md) · [Previous source section](unsupported-operating-systems.md) · [Next source section](api-and-feature-removals.md) · [Release/subject declaration](summary-release-highlights.md)
