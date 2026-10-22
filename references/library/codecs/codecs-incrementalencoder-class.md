# codecs: `codecs.IncrementalEncoder`

#### IncrementalEncoder Objects

The `IncrementalEncoder` class serves to encode an input over several steps. It defines the methods below, each of which every incremental encoder has to define so as to stay compatible with the Python codec registry.

 *class *codecs.IncrementalEncoder(*errors='strict'*)

Constructor for an `IncrementalEncoder` instance.

Every incremental encoder has to supply this constructor interface. They may add further keyword arguments of their own, but the Python codec registry uses only the ones defined here.

By accepting the *errors* keyword argument, the `IncrementalEncoder` can offer assorted error handling schemes. See Error Handlers for the values you can use.

The *errors* argument is assigned to an attribute bearing the same name. Because you can assign to that attribute, you may switch among different error handling strategies over the lifetime of the `IncrementalEncoder` object.

[Subject index](INDEX.md) · [Previous](incremental-encoding-and-decoding.md) · [Continue](incremental-encoder-operation-and-state.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
