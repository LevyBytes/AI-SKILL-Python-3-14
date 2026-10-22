# pickle — Out-of-band Buffers

### Out-of-band Buffers

Added in version 3.8.

In certain settings, the `pickle` module moves enormous quantities of data. As a result, holding the number of memory copies to a minimum can matter, in order to keep performance and resource usage in check. Yet the `pickle` module's ordinary operation, as it turns a graph-like arrangement of objects into a linear stream of bytes, fundamentally entails copying data into and out of the pickle stream.

You can dodge that constraint as long as the *provider* (the implementation of the object types being moved) together with the *consumer* (the implementation of the communications system) both back the out-of-band transfer facilities that pickle protocol 5 and above provide.

[Subject index](INDEX.md) · [Previous](custom-reduction-for-types-functions-and-other-objects.md) · [Continue](provider-api.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
