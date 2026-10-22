# Python 3.14.4 final / library / binascii

[gh-145264](https://github.com/python/cpython/issues/145264): The Base64 decoder (refer to [`binascii.a2b_base64()`](https://docs.python.org/3.14/library/binascii.html#binascii.a2b_base64), [`base64.b64decode()`](https://docs.python.org/3.14/library/base64.html#base64.b64decode), and so on) no longer disregards surplus data following the first padded quad while in non-strict (default) mode. Rather, matching [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html), section 3.3, it now disregards the pad character, "=", should it appear ahead of the end of the encoded data.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
