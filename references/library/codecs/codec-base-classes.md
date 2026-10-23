# codecs - Codec Base Classes

### Codec Base Classes

The `codecs` module supplies a family of base classes that lay out the interfaces for dealing with codec objects, and that can serve as the foundation for your own codec implementations.

For a codec to be usable in Python it has to define four interfaces: a stateless encoder, a stateless decoder, a stream reader, and a stream writer. As a rule the stream reader and writer lean on the stateless encoder/decoder to carry out the file protocols. Codec authors are likewise responsible for deciding how their codec deals with encoding and decoding errors.

[Subject index](INDEX.md) · [Previous](codecs-iterencode-to-codecs-bom-utf32-le.md) · [Continue](codecs-register-error-to-codecs-replace-errors.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
