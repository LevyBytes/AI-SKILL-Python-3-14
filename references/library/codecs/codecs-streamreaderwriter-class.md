# codecs - StreamReaderWriter Objects

#### StreamReaderWriter Objects

The `StreamReaderWriter` is a helper class for wrapping streams that operate in read and write modes alike.

It's arranged so that the factory functions handed back by the `lookup()` function can build the instance.

 *class *codecs.StreamReaderWriter(*stream*, *Reader*, *Writer*, *errors='strict'*)

Builds a `StreamReaderWriter` instance. Here *stream* has to be a file-like object. *Reader* and *Writer* have to be factory functions or classes that supply the `StreamReader` and `StreamWriter` interface respectively. Error handling proceeds just as it does for the stream readers and writers.

A `StreamReaderWriter` instance offers the merged interfaces of the `StreamReader` and `StreamWriter` classes. Every other method and attribute it inherits from the stream beneath it.

[Subject index](INDEX.md) · [Previous](codecs-streamreader-read-to-codecs-streamreader-reset.md) · [Continue](codecs-streamrecoder-class.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
