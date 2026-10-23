# codecs - Standalone Codec Functions

### Standalone Codec Functions

Encoding and decoding behavior much like a codec is offered by the functions below, though none of them is reachable as a named codec via `codecs.encode()` or `codecs.decode()`. Their use is internal (for instance, within [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle)), and they act much as the `string_escape` codec did before it was dropped in Python 3.

 codecs.escape_encode(*input*, *errors=None*)

Run *input* through escape-sequence encoding. This mirrors the way [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) applied to bytes yields escaped byte values.

A [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object is what *input* has to be.

Hands back a tuple `(output, length)` in which *output* is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object and *length* counts the bytes that were consumed.

 codecs.escape_decode(*input*, *errors=None*)

Take *input* back from its escape sequences to the bytes it started as.

A [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is what *input* has to be.

Hands back a tuple `(output, length)` in which *output* is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object and *length* counts the bytes that were consumed.

[Subject index](INDEX.md) · [Previous](binary-transforms.md) · [Continue](text-transforms.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
