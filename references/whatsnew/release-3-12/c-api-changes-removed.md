# What’s New In Python 3.12 / C API Changes / Removed

### Removed

- Drop the `token.h` header file. A public tokenizer C API never existed. That `token.h` header was intended solely for use inside Python internals. (Contributed by Victor Stinner in [gh-92651](https://github.com/python/cpython/issues/92651).)

- The legacy Unicode APIs are now gone. Consult [**PEP 623**](https://peps.python.org/pep-0623/) for the specifics.

  - `PyUnicode_WCHAR_KIND`

  - `PyUnicode_AS_UNICODE()`

  - `PyUnicode_AsUnicode()`

  - `PyUnicode_AsUnicodeAndSize()`

  - `PyUnicode_AS_DATA()`

  - `PyUnicode_FromUnicode()`

  - `PyUnicode_GET_SIZE()`

  - `PyUnicode_GetSize()`

  - `PyUnicode_GET_DATA_SIZE()`

- Drop the `PyUnicode_InternImmortal()` function macro. (Contributed by Victor Stinner in [gh-85858](https://github.com/python/cpython/issues/85858).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-deprecated-pending-removal-in-future-versions.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
