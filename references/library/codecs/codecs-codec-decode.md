# codecs / Stateless Encoding and Decoding: `decode()`

decode(*input*, *errors='strict'*)

Decodes the object *input* and returns a tuple (output object, length consumed). As one example, for a [text encoding](https://docs.python.org/3.14/glossary.html#term-text-encoding), decoding turns a bytes object that was encoded with a given character set encoding back into a string object.

Where a text encoding or a bytes-to-bytes codec is involved, *input* has to be a bytes object — or something that offers the read-only buffer interface, such as buffer objects and memory mapped files.

The *errors* argument sets which error handling to use. It defaults to `'strict'` handling.

This method must not stash state on the `Codec` instance. For codecs that have to retain state so decoding stays efficient, use `StreamReader`.

The decoder has to cope with zero length input and then return an empty object of the output object type.

[Subject index](INDEX.md) · [Previous](codecs-codec-class-to-encode.md) · [Continue](incremental-encoding-and-decoding.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md) · [Owning module, declaration or section: codecs.Codec; encode](codecs-codec-class-to-encode.md) · [Owning module, declaration or section: Stateless Encoding and Decoding](codecs-codec-class-to-encode.md)
