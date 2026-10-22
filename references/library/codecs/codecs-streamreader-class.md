# codecs: `codecs.StreamReader`

#### StreamReader Objects

`StreamReader` derives from `Codec` and supplies the methods below, every one of which a stream reader has to define to interoperate with the Python codec registry.

 *class *codecs.StreamReader(*stream*, *errors='strict'*)

Constructor for a `StreamReader` instance.

This constructor interface is mandatory for every stream reader. Readers may tack on further keyword arguments of their own, yet the Python codec registry relies solely on the ones specified here.

The *stream* argument has to be a file-like object opened for reading text or binary data, whichever suits the particular codec.

By supplying the *errors* keyword argument, the `StreamReader` can adopt various error handling schemes. Consult Error Handlers for the standard error handlers the stream codec underneath may accept.

The *errors* argument gets stored on an attribute that shares its name. Writing to that attribute lets you swap among differing error handling strategies across the `StreamReader` object's lifetime.

You can widen the collection of permitted values for the *errors* argument via `register_error()`.

[Subject index](INDEX.md) · [Previous](codecs-streamwriter-write-to-codecs-streamwriter-reset.md) · [Continue](codecs-streamreader-read-to-codecs-streamreader-reset.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
