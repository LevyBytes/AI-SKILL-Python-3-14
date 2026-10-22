# 10.9. Data compression

### 10.9. Data compression

Widely used archiving and compression formats get built-in handling from a set of modules, namely [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib), [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip), [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma), [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) and [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile).

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979

```

[Subject index](INDEX.md) · [Previous source section](dates-and-times.md) · [Following source section](performance-measurement.md)
