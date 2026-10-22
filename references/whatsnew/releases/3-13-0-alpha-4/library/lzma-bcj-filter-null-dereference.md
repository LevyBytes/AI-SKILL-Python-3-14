# Python 3.13.0 alpha 4 / library / fix null pointer dereference within lzma decode filter properties caused mishandling bcj

[gh-104282](https://github.com/python/cpython/issues/104282): Fix a null pointer dereference within `lzma._decode_filter_properties()` caused by mishandling BCJ filters whose properties have zero length. Radislav Chugunov wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
