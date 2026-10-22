# Python 3.8.0 alpha 4 / c api / sys

[bpo-36443](https://bugs.python.org/issue?@action=redirect&bpo=36443): Ever since Python 3.7.0, invoking [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) ahead of [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) yields mojibake when the `LC_CTYPE` locale is coerced and/or when the user's configuration switches on the UTF-8 Mode. To resolve that mojibake, the LC_CTYPE coercion along with UTF-8 Mode are now off by default. Turning them on now requires an explicit opt-in through the new `_Py_PreInitialize()` API together with `_PyPreConfig`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
