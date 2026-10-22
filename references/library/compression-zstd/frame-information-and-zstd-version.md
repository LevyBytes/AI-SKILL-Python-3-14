# Miscellaneous: `compression.zstd.FrameInfo`, `compression.zstd.COMPRESSION_LEVEL_DEFAULT`, `compression.zstd.zstd_version_info`

*class *compression.zstd.FrameInfo

Metadata pertaining to a Zstandard frame.

 decompressed_size

How large the frame’s decompressed contents are.

 dictionary_id

An integer standing for the Zstandard dictionary ID required to decompress the frame. A `0` signals that no dictionary ID was stored in the frame header — which could indicate either that no Zstandard dictionary is called for, or that a needed dictionary’s ID simply went unrecorded.

 compression.zstd.COMPRESSION_LEVEL_DEFAULT

Zstandard’s out-of-the-box compression level: `3`.

 compression.zstd.zstd_version_info

The runtime zstd library’s version number, given as an integer tuple of (major, minor, release).

[Subject index](INDEX.md) · [Previous](compression-zstd-get-frame-info.md) · [Continue](examples.md) · [Owning module, declaration or section: Miscellaneous](compression-zstd-get-frame-info.md)
