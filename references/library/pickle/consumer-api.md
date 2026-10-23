# pickle - Consumer API

### Consumer API

A communications system is able to turn on bespoke handling for the `PickleBuffer` objects that arise while an object graph is serialized.

On the sending end, it has to give `Pickler` (or the `dump()` or `dumps()` function) a *buffer_callback* argument, which gets invoked with each `PickleBuffer` produced while the object graph is pickled. Buffers gathered by the *buffer_callback* will not have their data copied into the pickle stream; only an inexpensive marker is placed there.

On the receiving end, it has to give `Unpickler` (or the `load()` or `loads()` function) a *buffers* argument, an iterable of the buffers that were handed to *buffer_callback*. That iterable must yield buffers in the very order they were given to *buffer_callback*. Those buffers supply the data the reconstructors of the objects expect — the objects whose pickling created the original `PickleBuffer` objects.

Between the sending end and the receiving end, the communications system is free to roll its own transfer mechanism for out-of-band buffers. Possible optimizations include relying on shared memory or on datatype-specific compression.

[Subject index](INDEX.md) · [Previous](provider-api.md) · [Continue](example.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
