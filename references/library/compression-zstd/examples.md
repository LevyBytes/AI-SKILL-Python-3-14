# Examples

### Examples

Reading in a compressed file:

```python
from compression import zstd

with zstd.open("file.zst") as f:
    file_content = f.read()

```

Creating a compressed file:

```python
from compression import zstd

data = b"Insert Data Here"
with zstd.open("file.zst", "w") as f:
    f.write(data)

```

Compressing data in memory:

```python
from compression import zstd

data_in = b"Insert Data Here"
data_out = zstd.compress(data_in)

```

Incremental compression:

```python
from compression import zstd

comp = zstd.ZstdCompressor()
out1 = comp.compress(b"Some data\n")
out2 = comp.compress(b"Another piece of data\n")
out3 = comp.compress(b"Even more data\n")
out4 = comp.flush()
# Concatenate all the partial results:
result = b"".join([out1, out2, out3, out4])

```

Writing compressed data to an already-open file:

```python
from compression import zstd

with open("myfile", "wb") as f:
    f.write(b"This data will not be compressed\n")
    with zstd.open(f, "w") as zstf:
        zstf.write(b"This *will* be compressed\n")
    f.write(b"Not compressed\n")

```

Creating a compressed file using compression parameters:

```python
from compression import zstd

options = {
   zstd.CompressionParameter.checksum_flag: 1
}
with zstd.open("file.zst", "w", options=options) as f:
    f.write(b"Mind if I squeeze in?")

```

[Subject index](INDEX.md) · [Previous](frame-information-and-zstd-version.md)
