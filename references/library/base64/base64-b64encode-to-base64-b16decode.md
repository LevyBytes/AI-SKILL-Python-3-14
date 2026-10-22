# base64 — RFC 4648 Encodings

### RFC 4648 Encodings

The [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) encodings work well for packaging binary data so that it travels safely through email, slots into URLs, or rides along inside an HTTP POST request.

 base64.b64encode(*s*, *altchars=None*)

Run Base64 over the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

When supplied, the optional *altchars* has to be a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) two bytes long, naming a substitute alphabet for the `+` and `/` characters. An application can lean on this to, say, build URL- or filesystem-safe Base64 strings. Its default value is `None`, under which the standard Base64 alphabet applies.

It may assert or throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the length of *altchars* isn't 2, and throws a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) should *altchars* fail to be a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

 base64.b64decode(*s*, *altchars=None*, *validate=False*)

Take the Base64-encoded [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string *s*, decode it, and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

The optional *altchars*, where given, has to be a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string two bytes long, naming the substitute alphabet that stands in for the `+` and `/` characters.

Should *s* carry incorrect padding, a [`binascii.Error`](https://docs.python.org/3.14/library/binascii.html#binascii.Error) exception is thrown.

With *validate* left at `False` (its default), any characters belonging to neither the normal base-64 alphabet nor the alternative one are dropped before the padding gets checked. Flip *validate* to `True`, and such non-alphabet characters in the input instead bring about a [`binascii.Error`](https://docs.python.org/3.14/library/binascii.html#binascii.Error).

To read more on the strict base64 check, turn to [`binascii.a2b_base64()`](https://docs.python.org/3.14/library/binascii.html#binascii.a2b_base64)

It may assert or throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the length of *altchars* isn't 2.

 base64.standard_b64encode(*s*)

Apply the standard Base64 alphabet to the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 base64.standard_b64decode(*s*)

Read the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string *s* through the standard Base64 alphabet and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 base64.urlsafe_b64encode(*s*)

Encode the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* through the URL- and filesystem-safe alphabet - the one that swaps `-` in for `+` and `_` in for `/` within the standard Base64 alphabet - and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). Even so, the output may still hold a `=`.

 base64.urlsafe_b64decode(*s*)

Decode the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string *s* through the URL- and filesystem-safe alphabet - the one that swaps `-` in for `+` and `_` in for `/` within the standard Base64 alphabet - and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 base64.b32encode(*s*)

Run Base32 over the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 base64.b32decode(*s*, *casefold=False*, *map01=None*)

Take the Base32-encoded [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string *s*, decode it, and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

The optional *casefold* flag says whether a lowercase alphabet may be fed in. For safety's sake, it defaults to `False`.

Under [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html), you may optionally map the digit 0 (zero) onto the letter O (oh), and likewise optionally map the digit 1 (one) onto either the letter I (eye) or the letter L (el). The optional *map01* argument, whenever it isn't `None`, picks which letter the digit 1 maps to (and once *map01* is something other than `None`, the digit 0 always maps to the letter O). On security grounds the default here is `None`, which keeps 0 and 1 out of the input altogether.

Where *s* is padded incorrectly, or where non-alphabet characters turn up in the input, a [`binascii.Error`](https://docs.python.org/3.14/library/binascii.html#binascii.Error) is thrown.

 base64.b32hexencode(*s*)

Behaves much like `b32encode()`, except that it draws on the Extended Hex Alphabet set out in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html).

Added in version 3.10.

 base64.b32hexdecode(*s*, *casefold=False*)

Behaves much like `b32decode()`, except that it draws on the Extended Hex Alphabet set out in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html).

In this variant the digit 0 (zero) to letter O (oh) and digit 1 (one) to letter I (eye) or letter L (el) mappings are disallowed, since every one of those characters belongs to the Extended Hex Alphabet and they may not be swapped for one another.

Added in version 3.10.

 base64.b16encode(*s*)

Run Base16 over the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 base64.b16decode(*s*, *casefold=False*)

Take the Base16-encoded [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string *s*, decode it, and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Here the optional *casefold* flag controls whether lowercase letters are permitted in the input. By default, and for the sake of security, it sits at `False`.

If *s* turns out to be padded wrongly, or if characters outside the alphabet appear in the input, the call throws a [`binascii.Error`](https://docs.python.org/3.14/library/binascii.html#binascii.Error).

[Subject index](INDEX.md) · [Previous](base64-base16-base32-base64-base85-data-encodings.md) · [Continue](base64-a85encode-to-base64-z85encode.md) · [Owning module, declaration or section: base64](base64-base16-base32-base64-base85-data-encodings.md)
