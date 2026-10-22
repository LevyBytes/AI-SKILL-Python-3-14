# What's New In Python 3.13 / New Deprecations — array, ctypes, decimal, dis, gettext

### New Deprecations

- [User-defined functions](https://docs.python.org/3.14/reference/datamodel.html#user-defined-funcs):

  - Deprecate assigning to a function's [`__code__`](https://docs.python.org/3.14/reference/datamodel.html#function.__code__) attribute when the incoming code object's type fails to match the function's own type. The four distinct types here are: plain function, generator, async generator, and coroutine. This change was contributed by Irit Katriel in [gh-81137](https://github.com/python/cpython/issues/81137).

- [`array`](https://docs.python.org/3.14/library/array.html#module-array):

  - Deprecate, at runtime, the `'u'` format code (`wchar_t`). Documentation has flagged this format code as deprecated since Python 3.3, and Python 3.16 will drop it. Reach for the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS4)) for Unicode characters in its place. (Contributed by Hugo van Kemenade in [gh-80480](https://github.com/python/cpython/issues/80480).)

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - Deprecate the undocumented `SetPointerType()` function, slated for removal in Python 3.15. (Contributed by Victor Stinner in [gh-105733](https://github.com/python/cpython/issues/105733).)

  - [Soft-deprecate](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) the [`ARRAY()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.ARRAY) function, preferring `type * length` multiplication. (Contributed by Victor Stinner in [gh-105733](https://github.com/python/cpython/issues/105733).)

- [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal):

  - Deprecate the non-standard, undocumented [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) format specifier `'N'`, which only the `decimal` module's C implementation supports. Its removal is planned for Python 3.18. (Contributed by Serhiy Storchaka in [gh-89902](https://github.com/python/cpython/issues/89902).)

- [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis):

  - Deprecate the `HAVE_ARGUMENT` separator. Test for membership in [`hasarg`](https://docs.python.org/3.14/library/dis.html#dis.hasarg) in its place. (Contributed by Irit Katriel in [gh-109319](https://github.com/python/cpython/issues/109319).)

- [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext):

  -

[Subject index](INDEX.md) · [Previous source section](webbrowser.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](plural-selection-and-library-deprecations.md)
