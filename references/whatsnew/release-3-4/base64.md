# What's New In Python 3.4 / base64 - base64

### base64

The encode and decode functions inside [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64) will now take any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) wherever they formerly demanded a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) instance. (Contributed by Nick Coghlan in [bpo-17839](https://bugs.python.org/issue?@action=redirect&bpo=17839).)

A set of new functions ? [`a85encode()`](https://docs.python.org/3.14/library/base64.html#base64.a85encode), [`a85decode()`](https://docs.python.org/3.14/library/base64.html#base64.a85decode), [`b85encode()`](https://docs.python.org/3.14/library/base64.html#base64.b85encode), and [`b85decode()`](https://docs.python.org/3.14/library/base64.html#base64.b85decode) ? let you encode and decode binary data to and from the `Ascii85` format and the git/mercurial `Base85` format, respectively. The `a85` functions expose options for matching the variants of the `Ascii85` encoding, the Adobe variant among them. (Work by Martin Morrison, plus the Mercurial project, Serhiy Storchaka, and Antoine Pitrou, landed under [bpo-17618](https://bugs.python.org/issue?@action=redirect&bpo=17618).)

[Subject index](INDEX.md) · [Previous source section](audioop.md) · [Next source section](collections.md) · [Release/subject declaration](release-highlights.md)
