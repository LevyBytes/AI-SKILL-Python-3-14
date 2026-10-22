# What's New In Python 3.3 / base64 — base64

### base64

The decoding functions of the [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64) modern interface will now take ASCII-only Unicode strings. As an example, `base64.b64decode('YWJj')` returns `b'abc'`. (Contributed by Catalin Iacob in [bpo-13641](https://bugs.python.org/issue?@action=redirect&bpo=13641).)

[Subject index](INDEX.md) · [Previous source section](array.md) · [Next source section](binascii.md) · [Release/subject declaration](summary-release-highlights.md)
