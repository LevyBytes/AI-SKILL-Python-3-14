# codecs - IncrementalDecoder Objects

#### IncrementalDecoder Objects

The `IncrementalDecoder` class serves to decode an input over several steps. It defines the methods below, each of which every incremental decoder has to define so as to stay compatible with the Python codec registry.

 *class *codecs.IncrementalDecoder(*errors='strict'*)

Constructor for an `IncrementalDecoder` instance.

Every incremental decoder has to supply this constructor interface. They may add further keyword arguments of their own, but the Python codec registry uses only the ones defined here.

By accepting the *errors* keyword argument, the `IncrementalDecoder` can offer assorted error handling schemes. See Error Handlers for the values you can use.

The *errors* argument is assigned to an attribute bearing the same name. Because you can assign to that attribute, you may switch among different error handling strategies over the lifetime of the `IncrementalDecoder` object.

[Subject index](INDEX.md) · [Previous](incremental-encoder-operation-and-state.md) · [Continue](codecs-incrementaldecoder-decode.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
