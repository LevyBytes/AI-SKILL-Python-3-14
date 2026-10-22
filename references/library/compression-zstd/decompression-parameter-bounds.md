# compression.zstd: `compression.zstd.DecompressionParameter`, `bounds()`

*class *compression.zstd.DecompressionParameter

An [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) that holds the advanced decompression parameter keys available while decompressing data. None of the parameters are required; whatever you leave out has its value chosen for you automatically.

To learn the permitted values for any parameter, call the `bounds()` method on its attribute.

Here the `window_log_max` is set to the largest size, by way of example:

```python
data = compress(b'Some very long buffer of bytes...')

_lower, upper = DecompressionParameter.window_log_max.bounds()

options = {DecompressionParameter.window_log_max: upper}
decompress(data, options=options)

```

 bounds()

Hand back a decompression parameter’s int bounds as the tuple `(lower, upper)`. You invoke this method on whichever attribute’s bounds you are after.

Each of the two bounds, lower and upper alike, is inclusive.

 window_log_max

The largest window size employed during decompression, taken as a base-two logarithm. It comes in handy for capping how much memory decompression consumes. The bigger that maximum window size, the quicker decompression runs.

Should this be zero, the value is settled automatically on your behalf.

[Subject index](INDEX.md) · [Previous](parallel-compression-job-controls.md) · [Continue](compression-zstd-strategy-class.md) · [Owning module, declaration or section: Advanced parameter control](compression-zstd-compressionparameter-class.md)
