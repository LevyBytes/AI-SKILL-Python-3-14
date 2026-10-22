# What's New In Python 3.10 / C API Changes / Deprecated

### Deprecated

- The `PyUnicode_InternImmortal()` function is deprecated now and is slated for removal in Python 3.12: turn to [`PyUnicode_InternInPlace()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternInPlace) instead. (Contributed by Victor Stinner in [bpo-41692](https://bugs.python.org/issue?@action=redirect&bpo=41692).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-porting-to-python-3-10.md) · [Next source section](c-api-changes-removed-removed.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-pep-652-maintaining-the-stable-abi.md)
