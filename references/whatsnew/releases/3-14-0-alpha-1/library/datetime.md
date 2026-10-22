# Python 3.14.0 alpha 1 / library / datetime

[gh-111513](https://github.com/python/cpython/issues/111513): Sharpens the error text that [`datetime.date.fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.fromtimestamp) might raise.

[gh-117398](https://github.com/python/cpython/issues/117398): Every object in the datetime C-API is now statically allocated, giving stronger memory safety, particularly across a module reload. Users should not notice any difference.

[gh-115225](https://github.com/python/cpython/issues/115225): Raise an error on a few technically legal yet pathological ISO 8601 strings handed to [`datetime.time.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.fromisoformat) that earlier got parsed wrongly.

[gh-102450](https://github.com/python/cpython/issues/102450): The ISO-8601 24:00 form, an alternative way to write midnight of the following day, is now accepted by [`datetime.datetime.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromisoformat) and [`datetime.time.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.fromisoformat). Izan “TizzySaurus” Robinson ([tizzysaurus@gmail.com](mailto:tizzysaurus%40gmail.com)) provided the patch

[gh-122272](https://github.com/python/cpython/issues/122272): On certain platforms, Linux among them, the century-bearing year went without 0-padding when [`strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strftime) used the C99-specific specifiers `'%C'` or `'%F'`. That 0-padding is now assured wherever the C library backs the `'%C'` and `'%F'` format specifiers. Patch by Ben Hsing

[gh-117398](https://github.com/python/cpython/issues/117398): The `_datetime` module (the C implementation behind [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime)) can now be imported across several interpreters.

[gh-120268](https://github.com/python/cpython/issues/120268): Refuse a `None` argument to the pure-Python [`datetime.date.fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.fromtimestamp), keeping it consistent with the C-extension version.

[gh-71587](https://github.com/python/cpython/issues/71587): Stop the crash in the C build of [`datetime.datetime.strptime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strptime) that struck when it was invoked once more on a restarted interpreter.

[gh-120161](https://github.com/python/cpython/issues/120161): [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) is no longer prone to crashing amid certain intricate reference-cycle scenarios.

[gh-120782](https://github.com/python/cpython/issues/120782): Corrected the bad references to the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) types that appeared once the module had been reloaded.

[gh-120713](https://github.com/python/cpython/issues/120713): On Linux, [`datetime.datetime.strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strftime) will now pad years shorter than four digits with leading zeros for the `%Y` and `%G` directives. Ben Hsing supplied the patch.

[gh-41431](https://github.com/python/cpython/issues/41431): Introduce [`datetime.time.strptime()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.strptime) along with [`datetime.date.strptime()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.strptime). Wannes Boeykens contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
