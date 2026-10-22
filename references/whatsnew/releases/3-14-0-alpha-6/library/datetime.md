# Python 3.14.0 alpha 6 / library / datetime

[gh-130959](https://github.com/python/cpython/issues/130959): Brings the pure-Python [`datetime.time.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.fromisoformat) into line with the C version by rejecting times whose fractional part holds spaces (for instance, `12:34:56.400 +02:00`). Micha? Gorny wrote this patch.

[gh-100388](https://github.com/python/cpython/issues/100388): The `platform._sys_version()` method has been fixed for the case where `__DATE__` is undefined at buildtime, by setting the default buildtime datetime string to the UNIX epoch.

[gh-107773](https://github.com/python/cpython/issues/107773): Makes the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) subclass [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) agree across both implementations. Semyon Moroz wrote this patch.

[gh-127260](https://github.com/python/cpython/issues/127260): Bans the colon (?:?) as a separator for the fractional component, along with further work to align how errors get raised between the C and Python versions of [`datetime.time.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.fromisoformat) and [`datetime.datetime.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromisoformat). Semyon Moroz wrote this patch.

[gh-109798](https://github.com/python/cpython/issues/109798): The [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) error messages now carry extra detail, and the wording was aligned so the C and Python implementations report it the same way. Semyon Moroz supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
