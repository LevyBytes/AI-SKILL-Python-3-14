# compression.zstd: `compression.zstd.train_dict()`, `compression.zstd.finalize_dict()`

### Zstandard dictionaries

 compression.zstd.train_dict(*samples*, *dict_size*)

Train a Zstandard dictionary, giving back a `ZstdDict` instance. Zstandard dictionaries let you compress smaller volumes of data more efficiently ? data that is normally hard to compress because it repeats so little. Where you compress many similar batches of data (for instance, files that resemble one another), Zstandard dictionaries can lift both compression ratios and speed by a wide margin.

For the *samples* argument (an iterable of [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects), supply the pool of samples that trains the Zstandard dictionary.

The *dict_size* argument, an integer, caps the size (in bytes) that the Zstandard dictionary may reach. The Zstandard documentation recommends a hard ceiling of no more than 100 KB, though the practical ceiling is often lower and depends on your data. Bigger dictionaries tend to slow compression down while raising compression ratios. Smaller dictionaries make compression quicker but trim the compression ratio.

 compression.zstd.finalize_dict(*zstd_dict*, */*, *samples*, *dict_size*, *level*)

An advanced function that turns a ?raw content? Zstandard dictionary into a regular Zstandard dictionary. A ?raw content? dictionary is simply a run of bytes with no obligation to obey the layout of a normal Zstandard dictionary.

The *zstd_dict* argument is a `ZstdDict` instance whose `dict_content` carries the raw dictionary contents.

For the *samples* argument (an iterable of [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects), provide the sample data from which the Zstandard dictionary is generated.

The *dict_size* argument, an integer, caps the size (in bytes) that the Zstandard dictionary may reach. Check `train_dict()` for guidance on how large the dictionary should get.

The *level* argument (an integer) is the compression level you expect to feed the compressors that use this dictionary. Because the dictionary information shifts from one compression level to the next, tuning it to the intended compression level can make compression more efficient.

[Subject index](INDEX.md) · [Previous](zstd-decompressor-and-decompression.md) · [Continue](compression-zstd-zstddict-class.md)
