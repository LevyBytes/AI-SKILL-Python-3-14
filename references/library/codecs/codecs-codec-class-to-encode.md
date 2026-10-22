# codecs / Stateless Encoding and Decoding: `codecs.Codec`, `encode()`

### Stateless Encoding and Decoding

The base `Codec` class defines the methods below, which double as the function interfaces of the stateless encoder and decoder:

 *class *codecs.Codec

 encode(*input*, *errors='strict'*)

Encodes the object *input* and returns a tuple (output object, length consumed). As one example, [text encoding](https://docs.python.org/3.14/glossary.html#term-text-encoding) turns a string object into a bytes object by means of a given character set encoding (e.g., `cp1252` or `iso-8859-1`).

The *errors* argument sets which error handling to use. It defaults to `'strict'` handling.

This method must not stash state on the `Codec` instance. For codecs that have to retain state so encoding stays efficient, use `StreamWriter`.

The encoder has to cope with zero length input and then return an empty object of the output object type.

[Subject index](INDEX.md) · [Previous](codecs-backslashreplace-errors-to-codecs-namereplace-errors.md) · [Continue](codecs-codec-decode.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
