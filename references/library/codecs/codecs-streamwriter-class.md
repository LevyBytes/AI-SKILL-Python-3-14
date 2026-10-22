# codecs: `codecs.StreamWriter`

#### StreamWriter Objects

`StreamWriter` derives from `Codec` and supplies the methods below, every one of which a stream writer has to define to interoperate with the Python codec registry.

 *class *codecs.StreamWriter(*stream*, *errors='strict'*)

Constructor for a `StreamWriter` instance.

This constructor interface is mandatory for every stream writer. Writers may tack on further keyword arguments of their own, yet the Python codec registry relies solely on the ones specified here.

The *stream* argument has to be a file-like object opened for writing text or binary data, whichever suits the particular codec.

By supplying the *errors* keyword argument, the `StreamWriter` can adopt various error handling schemes. Consult Error Handlers for the standard error handlers the stream codec underneath may accept.

The *errors* argument gets stored on an attribute that shares its name. Writing to that attribute lets you swap among differing error handling strategies across the `StreamWriter` object's lifetime.

[Subject index](INDEX.md) · [Previous](stream-encoding-and-decoding.md) · [Continue](codecs-streamwriter-write-to-codecs-streamwriter-reset.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
