# codecs — StreamRecoder Objects

#### StreamRecoder Objects

The `StreamRecoder` converts data from one encoding into another, which can come in handy when juggling differing encoding environments.

It's arranged so that the factory functions handed back by the `lookup()` function can build the instance.

 *class *codecs.StreamRecoder(*stream*, *encode*, *decode*, *Reader*, *Writer*, *errors='strict'*)

Builds a `StreamRecoder` instance that carries out a two-way conversion: *encode* and *decode* operate on the frontend — the data that code calling `read()` and `write()` sees — whereas *Reader* and *Writer* operate on the backend — the data residing in *stream*.

These objects let you perform see-through transcodings, say, from Latin-1 across to UTF-8 and the other way round.

The *stream* argument has to be a file-like object.

The *encode* and *decode* arguments have to conform to the `Codec` interface. *Reader* and *Writer* have to be factory functions or classes yielding objects with the `StreamReader` and `StreamWriter` interface.

Error handling proceeds just as it does for the stream readers and writers.

A `StreamRecoder` instance offers the merged interfaces of the `StreamReader` and `StreamWriter` classes. Every other method and attribute it inherits from the stream beneath it.

[Subject index](INDEX.md) · [Previous](codecs-streamreaderwriter-class.md) · [Continue](encodings-and-unicode.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
