# compression.zstd: `compression.zstd.Strategy`

*class *compression.zstd.Strategy

An [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) that gathers the compression strategies. A higher strategy number maps to compression that is more intricate and slower.

Note

There is no guarantee that the attribute values of `Strategy` stay constant from one zstd version to the next. What you can lean on is the attributes’ ordering alone. They appear below in that order.

The strategies on offer are:

 fast

 dfast

 greedy

 lazy

 lazy2

 btlazy2

 btopt

 btultra

 btultra2

[Subject index](INDEX.md) · [Previous](decompression-parameter-bounds.md) · [Continue](compression-zstd-get-frame-info.md) · [Owning module, declaration or section: Advanced parameter control](compression-zstd-compressionparameter-class.md)
