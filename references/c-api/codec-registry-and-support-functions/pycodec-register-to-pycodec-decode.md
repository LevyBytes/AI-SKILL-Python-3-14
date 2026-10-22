# Codec registry and support functions

# Codec, Complex

## Overview

Covers: Codec registry and support functions; Complex Number Objects.

## Codec registry and support functions

### Codec registry and support functions

 int PyCodec_Register([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *search_function)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Add a new codec search function to the registry.

A knock-on effect is that this attempts to import the `encodings` package, unless that has already happened, so that it stays at the head of the search-function list.

 int PyCodec_Unregister([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *search_function)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Remove a codec search function from the registry and wipe the registry's cache. Where the search function was never registered, take no action. Hand back 0 when it works. On error, raise an exception and hand back -1.

Added in version 3.10.

 int PyCodec_KnownEncoding(const char *encoding)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back `1` or `0` according to whether a codec stands registered for the given *encoding*. This function never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_Encode([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object, const char *encoding, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A generic, codec-driven encoding API.

*object* runs through whichever encoder function is located for the given *encoding*, applying the error handling approach named by *errors*. Pass `NULL` for *errors* to fall back on the codec's own default approach. A [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised should no encoder turn up.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_Decode([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object, const char *encoding, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A generic, codec-driven decoding API.

*object* runs through whichever decoder function is located for the given *encoding*, applying the error handling approach named by *errors*. Pass `NULL` for *errors* to fall back on the codec's own default approach. A [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised should no decoder turn up.

[Subject index](INDEX.md) · [Following source contract](pycodec-encoder-to-pycodec-streamwriter.md)
