# codecs: `codecs.encode()`, `codecs.decode()`, `codecs.charmap_build()`, `codecs.lookup()`

### `codecs` - Codec registry and base classes

**Source code:** [Lib/codecs.py](https://github.com/python/cpython/tree/3.14/Lib/codecs.py)

---

This module supplies base classes for the standard Python codecs (the encoders and decoders) and exposes the internal Python codec registry, which drives the lookup of codecs and of error handlers. While the bulk of the standard codecs are [text encodings](https://docs.python.org/3.14/glossary.html#term-text-encoding) that turn text into bytes (and bytes back into text), the module also ships codecs that go text-to-text and bytes-to-bytes. Although your own custom codecs may translate between arbitrary types, a handful of the module's features apply only to text encodings or only to codecs whose output is [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

For encoding and decoding with any codec, the module exposes the functions below:

 codecs.encode(*obj*, *encoding='utf-8'*, *errors='strict'*)

Encodes *obj* using the codec registered for *encoding*.

You may supply *errors* to choose the error handling scheme you want. The fallback handler is `'strict'`, which means that an encoding failure raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) (or a more codec specific subclass, such as [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError)). See Codec Base Classes for further detail on how codecs treat errors.

 codecs.decode(*obj*, *encoding='utf-8'*, *errors='strict'*)

Decodes *obj* using the codec registered for *encoding*.

You may supply *errors* to choose the error handling scheme you want. The fallback handler is `'strict'`, which means that a decoding failure raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) (or a more codec specific subclass, such as [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError)). See Codec Base Classes for further detail on how codecs treat errors.

 codecs.charmap_build(*string*)

Produce a mapping fit for encoding via a custom single-byte encoding. Given a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) *string* of as many as 256 characters that represent a decoding table, the call yields either the compact internal mapping object `EncodingMap` or a [`dictionary`](https://docs.python.org/3.14/library/stdtypes.html#dict) that maps character ordinals onto byte values. Invalid input triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

You can also query the complete details of any individual codec directly:

 codecs.lookup(*encoding*, */*)

Searches the Python codec registry for the codec info and yields a `CodecInfo` object of the shape laid out below.

The registry's cache is consulted first when resolving an encoding. On a cache miss, each registered search function is tried in turn. Should no `CodecInfo` object turn up, a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised. Otherwise the resulting `CodecInfo` object is cached and handed back to the caller.

[Subject index](INDEX.md) · [Continue](codecs-codecinfo-class.md)
