# codecs - Incremental Encoding and Decoding

### Incremental Encoding and Decoding

The `IncrementalEncoder` and `IncrementalDecoder` classes lay out the basic interface for incremental encoding and decoding. Here the input is encoded or decoded not through a single call to the stateless encoder/decoder function but across several calls to the `encode()`/`decode()` method of the incremental encoder/decoder, which tracks the encoding/decoding process from one call to the next.

Concatenating the output of the successive `encode()`/`decode()` calls yields the same result as if every separate input had been joined into one and that single input had been run through the stateless encoder/decoder.

[Subject index](INDEX.md) · [Previous](codecs-codec-decode.md) · [Continue](codecs-incrementalencoder-class.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
