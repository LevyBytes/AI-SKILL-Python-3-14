# lzma - Miscellaneous

### Miscellaneous

 lzma.is_check_supported(*check*)

Hand back `True` when the named integrity check has support on the current system.

Support for `CHECK_NONE` and `CHECK_CRC32` is always present. By contrast, `CHECK_CRC64` and `CHECK_SHA256` might be missing should your build of **liblzma** have been compiled with a pared-down feature set.

[Subject index](INDEX.md) · [Previous](lzma-compress-to-lzma-decompress.md) · [Continue](specifying-custom-filter-chains.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md)
