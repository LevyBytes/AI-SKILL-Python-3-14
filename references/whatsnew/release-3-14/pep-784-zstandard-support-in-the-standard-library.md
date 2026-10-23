# What's new in Python 3.14 / **PEP 784**: Zstandard support in the standard library - bz2, gzip, lzma, shutil, tarfile, zipfile, zlib

### [**PEP 784**](https://peps.python.org/pep-0784/): Zstandard support in the standard library

A fresh `compression` package now bundles the modules `compression.lzma`, `compression.bz2`, `compression.gzip` and `compression.zlib`, each of which re-exports the [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma), [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) and [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) modules in turn. Starting with Python 3.14, the recommended way to bring in these compression modules is through the new `compression` import names. That said, the older module names remain available and carry no deprecation. Should the legacy compression modules ever be deprecated or dropped, it will happen at least five years past the 3.14 release.

For the Zstandard format, the new `compression.zstd` module exposes compression plus decompression APIs by binding to [Meta’s zstd library](https://facebook.github.io/zstd/). Zstandard ranks among the broadly used, highly efficient, and fast compression formats. Beyond the APIs that `compression.zstd` brings in, the ability to read and write archives compressed with Zstandard now extends to the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile), [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile), and [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) modules.

The snippet below shows the new module compressing a bit of data:

```python
from compression import zstd
import math

data = str(math.pi).encode() * 20
compressed = zstd.compress(data)
ratio = len(compressed) / len(data)
print(f"Achieved compression ratio of {ratio}")

```

You can observe that this API resembles those of the `lzma` and `bz2` modules.

> (Contributed by Emma Harper Smith, Adam Turner, Gregory P. Smith, Tomas Roun, Victor Stinner, and Rogdham in [gh-132983](https://github.com/python/cpython/issues/132983).)

See also

[**PEP 784**](https://peps.python.org/pep-0784/).

[Subject index](INDEX.md) · [Previous source section](unhashable-object-error-diagnostics.md) · [Next source section](asyncio-introspection-capabilities.md) · [Release/subject declaration](summary-release-highlights.md)
