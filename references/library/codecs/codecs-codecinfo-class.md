# codecs: `codecs.CodecInfo`

*class *codecs.CodecInfo(*encode*, *decode*, *streamreader=None*, *streamwriter=None*, *incrementalencoder=None*, *incrementaldecoder=None*, *name=None*)

Holds the codec details produced by a registry lookup. Each constructor argument is kept in an attribute that carries its own name:

 name

The name of the encoding.

 encode

 decode

The stateless encoding and decoding functions. Each must be a function or method exposing the same interface as the `encode()` and `decode()` methods carried by Codec instances (see Codec Interface). They are expected to operate in a stateless fashion.

 incrementalencoder

 incrementaldecoder

Incremental encoder and decoder classes or factory functions. Each is required to supply the interface laid out by the base classes `IncrementalEncoder` and `IncrementalDecoder`, respectively. Incremental codecs are permitted to retain state.

 streamwriter

 streamreader

Stream writer and reader classes or factory functions. Each is required to supply the interface laid out by the base classes `StreamWriter` and `StreamReader`, respectively. Stream codecs are permitted to retain state.

To make the individual codec components easier to reach, the module offers the extra functions below, all of which rely on `lookup()` for the codec lookup:

[Subject index](INDEX.md) · [Previous](codecs-encode-to-codecs-lookup.md) · [Continue](codecs-getencoder-to-codecs-encodedfile.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
