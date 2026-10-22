# Python 3.10.0 alpha 7 / core and builtins / sys

[bpo-35883](https://bugs.python.org/issue?@action=redirect&bpo=35883): A command-line argument holding an invalid Unicode character will no longer cause Python to abort at startup with a fatal error. The [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) function now escapes any byte sequences that would otherwise decode into Unicode characters beyond the [U+0000; U+10ffff] range.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
