# Quopri

# Quopri

### `quopri` — Encode and decode MIME quoted-printable data

**Source code:** [Lib/quopri.py](https://github.com/python/cpython/tree/3.14/Lib/quopri.py)

---

Here you get quoted-printable transport encoding plus decoding, following the specification laid out in [**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html) — its Part One, which covers MIME (Multipurpose Internet Mail Extensions) and the mechanisms used to specify and describe how Internet message bodies are formatted. Use this scheme when a payload holds only a small proportion of nonprintable bytes; should the data instead carry many such bytes — a graphics file being the classic case — the tighter base64 approach offered through the [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64) module wins on size.

`quopri.decode(*input*, *output*, *header=False*)`

Reads from the *input* file, then deposits the recovered binary bytes into *output*. Both *input* and *output* are required to be [binary file objects](https://docs.python.org/3.14/glossary.html#term-file-object). Should the optional *header* argument be supplied with a true value, every underscore turns back into a space — the convention for unpacking “Q”-encoded headers spelled out in [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html) — Part Two of MIME (Multipurpose Internet Mail Extensions), the portion describing header extensions that carry non-ASCII text.

`quopri.encode(*input*, *output*, *quotetabs*, *header=False*)`

Reads from the *input* file and emits the corresponding quoted-printable bytes into *output*; again, both *input* and *output* have to be [binary file objects](https://docs.python.org/3.14/glossary.html#term-file-object). The mandatory *quotetabs* flag decides how interior spaces and tabs are handled: a true value escapes that embedded whitespace, while a false value passes it through untouched. Keep in mind that any space or tab sitting at a line's end is escaped regardless, exactly as [**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html) mandates. The *header* flag, meanwhile, governs whether spaces become underscores per [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html).

`quopri.decodestring(*s*, *header=False*)`

Mirrors `decode()`, but takes a source [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) value and hands back the decoded `bytes`.

`quopri.encodestring(*s*, *quotetabs=False*, *header=False*)`

Mirrors `encode()`, but takes a source [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) value and hands back the encoded `bytes`. Unless told otherwise, it passes a `False` value through to the *quotetabs* parameter of the `encode()` function.

See also

Module [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64)

Encoding and decoding for MIME base64 data

[Subject index](INDEX.md)
