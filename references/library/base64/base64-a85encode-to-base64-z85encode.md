# base64: `base64.a85encode()`, `base64.a85decode()`, `base64.b85encode()`, `base64.b85decode()`, `base64.z85encode()`

### Base85 Encodings

Base85 encoding names a whole family of algorithms that pack four bytes into five ASCII characters apiece. It first appeared in the Unix `btoa(1)` utility; later Adobe took up a version of it within the PostScript language, and it is now standardized in PDF 2.0 (ISO 32000-2). That version, across both its `btoa` and PDF forms, is what `a85encode()` carries out.

A different version, built on another output character set, started life as an April Fool's joke in [**RFC 1924**](https://datatracker.ietf.org/doc/html/rfc1924.html), yet Git and other software now put it to real use. This one is what `b85encode()` carries out.

A third version, lastly, relies on still another output character set tailored for dropping safely into programming-language strings; ZeroMQ defines it, and here `z85encode()` carries it out.

Across this module, the functions part ways over how they deal with the points below:

- Whether the surrounding `<~` and `~>` markers are emitted and expected.

- Whether the input gets folded across several lines.

- Which collection of ASCII characters serves for encoding.

- Tight encodings for stretches of spaces and null bytes.

- How zero-padding bytes tacked onto the input are encoded.

For fuller detail, consult the documentation of each function on its own.

 base64.a85encode(*b*, ***, *foldspaces=False*, *wrapcol=0*, *pad=False*, *adobe=False*)

Run Ascii85 over the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *b* and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

The optional *foldspaces* flag swaps in the special short sequence ‘y’ in place of 4 consecutive spaces (ASCII 0x20), the way ‘btoa’ does. PDF's standard encoding offers no such capability.

*wrapcol* decides whether newline (`b'\n'`) characters get tacked onto the output. When it is non-zero, no output line runs longer than that many characters, the trailing newline aside.

*pad* decides whether the zero-padding added at the input's tail is kept whole in the encoded output, the way `btoa` does, yielding output that is an exact multiple of 5 bytes. PDF's standard encoding leaves this out, since it doesn't hold onto the data's length.

*adobe* decides whether the encoded byte sequence gets wrapped in `<~` and `~>`, just as a PostScript base-85 string literal would. Bear in mind that ASCII85Decode streams within PDF documents *must* close with `~>`, yet they *must not* open with a leading `<~`.

Added in version 3.4.

 `base64.a85decode(*b*, ***, *foldspaces=False*, *adobe=False*, *ignorechars=b' \t\n\r\x0b'*)`

Take the Ascii85-encoded [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string *b*, decode it, and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

The *foldspaces* flag sets whether the ‘y’ short sequence is taken as shorthand for 4 consecutive spaces (ASCII 0x20). The standard Ascii85 encoding of PDF and PostScript provides no such capability.

*adobe* sets whether the `<~` and `~>` markers appear. The opening `<~` isn't mandatory, but the input has to finish with `~>`, or else a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets thrown.

*ignorechars* ought to be a byte string listing characters that the input should skip over. Confine it to whitespace characters; by default it holds every ASCII whitespace character.

Added in version 3.4.

 base64.b85encode(*b*, *pad=False*)

Run base85 (the flavor seen in, for instance, git-style binary diffs) over the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *b* and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Before encoding, the input gets padded out with `b'\0'` until its length divides evenly by 4 bytes. Set *pad* to true and every resulting character stays in the output, which then always comes to a multiple of 5 bytes - meaning the data's length might not survive a round trip through decoding.

Added in version 3.4.

 base64.b85decode(*b*)

Take the base85-encoded [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or ASCII string *b*, decode it, and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Added in version 3.4.

 base64.z85encode(*s*)

Run Z85 (the encoding ZeroMQ uses) over the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Per the [ZeroMQ specification](https://rfc.zeromq.org/spec/32/), Z85-encoded data has to come to a length that divides evenly by 5 bytes. So that your data frames stay compliant, pad the input you feed this function out to a multiple of 4 bytes.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](base64-b64encode-to-base64-b16decode.md) · [Continue](base64-z85decode.md) · [Owning module, declaration or section: base64](base64-base16-base32-base64-base85-data-encodings.md)
