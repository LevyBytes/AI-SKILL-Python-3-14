# pickle - Provider API

### Provider API

Each large data object headed for pickling has to provide a `__reduce_ex__()` method tailored to protocol 5 and above, one that hands back a `PickleBuffer` instance (rather than, say, a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object) for any sizeable data.

A `PickleBuffer` object *signals* that its underlying buffer qualifies for out-of-band data transfer. Such objects stay compatible with ordinary use of the `pickle` module. Consumers, however, may also opt in to tell `pickle` that they will manage those buffers themselves.

[Subject index](INDEX.md) · [Previous](out-of-band-buffers.md) · [Continue](consumer-api.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
