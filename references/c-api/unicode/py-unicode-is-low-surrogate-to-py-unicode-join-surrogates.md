# unicode C API: `Py_UNICODE_IS_LOW_SURROGATE()`, `Py_UNICODE_HIGH_SURROGATE()`, `Py_UNICODE_LOW_SURROGATE()`, `Py_UNICODE_JOIN_SURROGATES()`

int Py_UNICODE_IS_LOW_SURROGATE(Py_UCS4 ch)

Test whether *ch* is a low surrogate (`0xDC00 <= ch <= 0xDFFF`).

 Py_UCS4 Py_UNICODE_HIGH_SURROGATE(Py_UCS4 ch)

Gives the high UTF-16 surrogate (`0xD800` to `0xDBFF`) corresponding to a Unicode code point within the range `[0x10000; 0x10FFFF]`.

 Py_UCS4 Py_UNICODE_LOW_SURROGATE(Py_UCS4 ch)

Gives the low UTF-16 surrogate (`0xDC00` to `0xDFFF`) corresponding to a Unicode code point within the range `[0x10000; 0x10FFFF]`.

 Py_UCS4 Py_UNICODE_JOIN_SURROGATES(Py_UCS4 high, Py_UCS4 low)

Combines a pair of surrogate code points and gives back one `Py_UCS4` value. Within a surrogate pair, *high* is the leading surrogate and *low* the trailing one. The *high* argument must land in the range `[0xD800; 0xDBFF]`, while *low* must land in the range `[0xDC00; 0xDFFF]`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-unicode-isspace-to-py-unicode-is-high-surrogate.md) · [Following source contract](pyunicode-new-to-pyunicode-fromstring.md)
