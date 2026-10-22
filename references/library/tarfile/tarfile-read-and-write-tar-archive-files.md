# tarfile: Tar archive capabilities and format overview

### `tarfile` — Read and write tar archive files

**Source code:** [Lib/tarfile.py](https://github.com/python/cpython/tree/3.14/Lib/tarfile.py)

---

With the `tarfile` module you can both read from and write to tar archives, including the gzip, bz2 and lzma compressed variants. To handle `.zip` files instead, reach for the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) module, or use the more abstract helpers in [shutil](https://docs.python.org/3.14/library/shutil.html#archiving-operations).

A summary of what it offers:

- reads and writes [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip), [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd), and [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) compressed archives if the respective modules are available.

Should any of these [optional modules](https://docs.python.org/3.14/glossary.html#term-optional-module) be absent from your build of CPython, consult the documentation supplied by your distributor (in other words, whoever handed Python to you). Distributors themselves should refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

- read/write support for the POSIX.1-1988 (ustar) format.

- read/write support for the GNU tar format, covering the *longname* and *longlink* extensions; read-only support across every variant of the *sparse* extension, sparse-file restoration included.

- read/write support for the POSIX.1-2001 (pax) format.

- copes with directories, regular files, and hardlinks, plus symbolic links, fifos, character devices, and block devices, and it can capture then restore file metadata such as timestamp, access permissions and owner.

Changed in version 3.3: Added support for [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) compression.

Changed in version 3.12: A filter now drives archive extraction, letting you either rein in surprising/dangerous features or signal that such features are expected because the archive is fully trusted.

Changed in version 3.14: The extraction filter now defaults to `data`, which bars certain risky behaviors, among them links pointing at absolute paths or at paths beyond the destination. Earlier the filter behavior matched `fully_trusted`.

Changed in version 3.14: Added support for Zstandard compression using [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd).

[Subject index](INDEX.md) · [Continue](tarfile-open.md)
