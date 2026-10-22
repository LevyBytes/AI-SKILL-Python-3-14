# base64 — `base64` — Base16, Base32, Base64, Base85 Data Encodings

# Base64

### `base64` — Base16, Base32, Base64, Base85 Data Encodings

**Source code:** [Lib/base64.py](https://github.com/python/cpython/tree/3.14/Lib/base64.py)

---

Here you get functions that turn binary data into printable ASCII characters and turn those encodings back into binary data again. The set covers the encodings laid out in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) (Base64, Base32 and Base16), the Base85 encoding from [PDF 2.0](https://pdfa.org/resource/iso-32000-2/), plus the non-standard Base85 flavors found elsewhere.

The module hands you two separate interfaces. With the modern one you can encode [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) into ASCII [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and decode bytes-like objects or ASCII-bearing strings down to `bytes`. It handles each of the two base-64 alphabets from [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) - the normal one and the URL- and filesystem-safe one.

By contrast, the legacy interface can't decode out of strings, yet it does give you functions to encode and decode against [file objects](https://docs.python.org/3.14/glossary.html#term-file-object). Limited to the Base64 standard alphabet alone, it inserts newlines at every 76 characters in keeping with [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html). Keep in mind that if it's [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) support you're after, the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package is most likely the better place to look.

Changed in version 3.3: The modern interface's decoding functions will now take ASCII-only Unicode strings.

Changed in version 3.4: Every encoding and decoding function in the module now takes any [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Ascii85/Base85 support added.

[Subject index](INDEX.md) · [Continue](base64-b64encode-to-base64-b16decode.md)
