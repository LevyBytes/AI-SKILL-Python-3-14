# bdb — Binary Data Services

## Binary Data Services??

### Binary Data Services

This chapter's modules supply some basic services operations for working with binary data. Further operations on binary data, in particular those concerning file formats and network protocols, appear in the relevant sections.

Certain libraries covered under [Text Processing Services](https://docs.python.org/3.14/library/text.html#textservices) operate as well on either ASCII-compatible binary formats (for instance, [`re`](https://docs.python.org/3.14/library/re.html#module-re)) or all binary data (for instance, [`difflib`](https://docs.python.org/3.14/library/difflib.html#module-difflib)).

Beyond that, consult the documentation for Python's built-in binary data types in [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3.14/library/stdtypes.html#binaryseq).

- [`struct` — Interpret bytes as packed binary data](https://docs.python.org/3.14/library/struct.html)
  - [Functions and Exceptions](https://docs.python.org/3.14/library/struct.html#functions-and-exceptions)
  - [Format Strings](https://docs.python.org/3.14/library/struct.html#format-strings)
    - [Byte Order, Size, and Alignment](https://docs.python.org/3.14/library/struct.html#byte-order-size-and-alignment)
    - [Format Characters](https://docs.python.org/3.14/library/struct.html#format-characters)
    - [Examples](https://docs.python.org/3.14/library/struct.html#examples)

  - [Applications](https://docs.python.org/3.14/library/struct.html#applications)
    - [Native Formats](https://docs.python.org/3.14/library/struct.html#native-formats)
    - [Standard Formats](https://docs.python.org/3.14/library/struct.html#standard-formats)

  - [Classes](https://docs.python.org/3.14/library/struct.html#classes)

- [`codecs` — Codec registry and base classes](https://docs.python.org/3.14/library/codecs.html)
  - [Codec Base Classes](https://docs.python.org/3.14/library/codecs.html#codec-base-classes)
    - [Error Handlers](https://docs.python.org/3.14/library/codecs.html#error-handlers)
    - [Stateless Encoding and Decoding](https://docs.python.org/3.14/library/codecs.html#stateless-encoding-and-decoding)
    - [Incremental Encoding and Decoding](https://docs.python.org/3.14/library/codecs.html#incremental-encoding-and-decoding)
      - [IncrementalEncoder Objects](https://docs.python.org/3.14/library/codecs.html#incrementalencoder-objects)
      - [IncrementalDecoder Objects](https://docs.python.org/3.14/library/codecs.html#incrementaldecoder-objects)

    - [Stream Encoding and Decoding](https://docs.python.org/3.14/library/codecs.html#stream-encoding-and-decoding)
      - [StreamWriter Objects](https://docs.python.org/3.14/library/codecs.html#streamwriter-objects)
      - [StreamReader Objects](https://docs.python.org/3.14/library/codecs.html#streamreader-objects)
      - [StreamReaderWriter Objects](https://docs.python.org/3.14/library/codecs.html#streamreaderwriter-objects)
      - [StreamRecoder Objects](https://docs.python.org/3.14/library/codecs.html#streamrecoder-objects)

  - [Encodings and Unicode](https://docs.python.org/3.14/library/codecs.html#encodings-and-unicode)
  - [Standard Encodings](https://docs.python.org/3.14/library/codecs.html#standard-encodings)
  - [Python Specific Encodings](https://docs.python.org/3.14/library/codecs.html#python-specific-encodings)
    - [Text Encodings](https://docs.python.org/3.14/library/codecs.html#text-encodings)
    - [Binary Transforms](https://docs.python.org/3.14/library/codecs.html#binary-transforms)
    - [Standalone Codec Functions](https://docs.python.org/3.14/library/codecs.html#standalone-codec-functions)
    - [Text Transforms](https://docs.python.org/3.14/library/codecs.html#text-transforms)

  - [`encodings` — Encodings package](https://docs.python.org/3.14/library/codecs.html#module-encodings)
  - [`encodings.idna` — Internationalized Domain Names in Applications](https://docs.python.org/3.14/library/codecs.html#module-encodings.idna)
  - [`encodings.mbcs` — Windows ANSI codepage](https://docs.python.org/3.14/library/codecs.html#module-encodings.mbcs)
  - [`encodings.utf_8_sig` — UTF-8 codec with BOM signature](https://docs.python.org/3.14/library/codecs.html#module-encodings.utf_8_sig)

[Subject index](INDEX.md)
