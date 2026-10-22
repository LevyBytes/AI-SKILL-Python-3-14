# What's New In Python 3.6 / Deprecated functions and types of the C API

### Deprecated functions and types of the C API

The undocumented functions `PyUnicode_AsEncodedObject()`, `PyUnicode_AsDecodedObject()`, `PyUnicode_AsEncodedUnicode()` and `PyUnicode_AsDecodedUnicode()` carry a deprecation now. Reach for the [generic codec based API](https://docs.python.org/3.14/c-api/codec.html#codec-registry) in their place.

[Subject index](INDEX.md) · [Previous source section](xml.md) · [Next source section](deprecated-build-options.md) · [Release/subject declaration](summary-release-highlights.md)
