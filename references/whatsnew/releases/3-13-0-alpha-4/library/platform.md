# Python 3.13.0 alpha 4 / library / platform

[gh-110190](https://github.com/python/cpython/issues/110190): Repair ctypes structs containing an array on the Windows ARM64 platform by assigning `MAX_STRUCT_SIZE` the value 32 inside stgdict. Diego Russo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
