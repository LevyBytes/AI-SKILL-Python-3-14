# compression.zstd: `compression.zstd.CompressionParameter`

### Advanced parameter control

 *class *compression.zstd.CompressionParameter

An [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) holding the advanced compression parameter keys you can apply while compressing data.

Call the `bounds()` method on any attribute to learn the valid values for that parameter.

Parameters are optional; whatever parameter you leave out will have its value chosen automatically.

Example getting the lower and upper bound of `compression_level`:

```python
lower, upper = CompressionParameter.compression_level.bounds()

```

Example setting the `window_log` to the maximum size:

```python
_lower, upper = CompressionParameter.window_log.bounds()
options = {CompressionParameter.window_log: upper}
compress(b'venezuelan beaver cheese', options=options)

```

[Subject index](INDEX.md) · [Previous](compression-zstd-zstddict-class.md) · [Continue](compression-zstd-compressionparameter-bounds.md)
