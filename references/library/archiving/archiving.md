# Archiving

# Archiving

### Data Compression and Archiving

This chapter's modules provide data compression through the zlib, gzip, bzip2, lzma, and zstd algorithms, plus the building of archives in ZIP and tar formats. Refer as well to the [Archiving operations](https://docs.python.org/3.14/library/shutil.html#archiving-operations) that the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module offers.

- [The `compression` package](https://docs.python.org/3.14/library/compression.html)
- [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3.14/library/compression.zstd.html)
  - [Exceptions](https://docs.python.org/3.14/library/compression.zstd.html#exceptions)
  - [Reading and writing compressed files](https://docs.python.org/3.14/library/compression.zstd.html#reading-and-writing-compressed-files)
  - [Compressing and decompressing data in memory](https://docs.python.org/3.14/library/compression.zstd.html#compressing-and-decompressing-data-in-memory)
  - [Zstandard dictionaries](https://docs.python.org/3.14/library/compression.zstd.html#zstandard-dictionaries)
  - [Advanced parameter control](https://docs.python.org/3.14/library/compression.zstd.html#advanced-parameter-control)
  - [Miscellaneous](https://docs.python.org/3.14/library/compression.zstd.html#miscellaneous)
  - [Examples](https://docs.python.org/3.14/library/compression.zstd.html#examples)

- [`zlib` — Compression compatible with **gzip**](https://docs.python.org/3.14/library/zlib.html)
- [`gzip` — Support for **gzip** files](https://docs.python.org/3.14/library/gzip.html)
  - [Examples of usage](https://docs.python.org/3.14/library/gzip.html#examples-of-usage)
  - [Command-line interface](https://docs.python.org/3.14/library/gzip.html#command-line-interface)
    - [Command-line options](https://docs.python.org/3.14/library/gzip.html#command-line-options)

- [`bz2` — Support for **bzip2** compression](https://docs.python.org/3.14/library/bz2.html)
  - [(De)compression of files](https://docs.python.org/3.14/library/bz2.html#de-compression-of-files)
  - [Incremental (de)compression](https://docs.python.org/3.14/library/bz2.html#incremental-de-compression)
  - [One-shot (de)compression](https://docs.python.org/3.14/library/bz2.html#one-shot-de-compression)
  - [Examples of usage](https://docs.python.org/3.14/library/bz2.html#examples-of-usage)

- [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3.14/library/lzma.html)
  - [Reading and writing compressed files](https://docs.python.org/3.14/library/lzma.html#reading-and-writing-compressed-files)
  - [Compressing and decompressing data in memory](https://docs.python.org/3.14/library/lzma.html#compressing-and-decompressing-data-in-memory)
  - [Miscellaneous](https://docs.python.org/3.14/library/lzma.html#miscellaneous)
  - [Specifying custom filter chains](https://docs.python.org/3.14/library/lzma.html#specifying-custom-filter-chains)
  - [Examples](https://docs.python.org/3.14/library/lzma.html#examples)

- [`zipfile` — Work with ZIP archives](https://docs.python.org/3.14/library/zipfile.html)
  - [ZipFile objects](https://docs.python.org/3.14/library/zipfile.html#zipfile-objects)
  - [Path objects](https://docs.python.org/3.14/library/zipfile.html#path-objects)
  - [PyZipFile objects](https://docs.python.org/3.14/library/zipfile.html#pyzipfile-objects)
  - [ZipInfo objects](https://docs.python.org/3.14/library/zipfile.html#zipinfo-objects)
  - [Command-line interface](https://docs.python.org/3.14/library/zipfile.html#command-line-interface)
    - [Command-line options](https://docs.python.org/3.14/library/zipfile.html#command-line-options)

  - [Decompression pitfalls](https://docs.python.org/3.14/library/zipfile.html#decompression-pitfalls)
    - [From file itself](https://docs.python.org/3.14/library/zipfile.html#from-file-itself)
    - [File system limitations](https://docs.python.org/3.14/library/zipfile.html#file-system-limitations)
    - [Resources limitations](https://docs.python.org/3.14/library/zipfile.html#resources-limitations)
    - [Interruption](https://docs.python.org/3.14/library/zipfile.html#interruption)
    - [Default behaviors of extraction](https://docs.python.org/3.14/library/zipfile.html#default-behaviors-of-extraction)

- [`tarfile` — Read and write tar archive files](https://docs.python.org/3.14/library/tarfile.html)
  - [TarFile Objects](https://docs.python.org/3.14/library/tarfile.html#tarfile-objects)
  - [TarInfo Objects](https://docs.python.org/3.14/library/tarfile.html#tarinfo-objects)
  - [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#extraction-filters)
    - [Default named filters](https://docs.python.org/3.14/library/tarfile.html#default-named-filters)
    - [Filter errors](https://docs.python.org/3.14/library/tarfile.html#filter-errors)
    - [Hints for further verification](https://docs.python.org/3.14/library/tarfile.html#hints-for-further-verification)
    - [Supporting older Python versions](https://docs.python.org/3.14/library/tarfile.html#supporting-older-python-versions)
    - [Stateful extraction filter example](https://docs.python.org/3.14/library/tarfile.html#stateful-extraction-filter-example)

  - [Command-Line Interface](https://docs.python.org/3.14/library/tarfile.html#command-line-interface)
    - [Command-line options](https://docs.python.org/3.14/library/tarfile.html#command-line-options)

  - [Examples](https://docs.python.org/3.14/library/tarfile.html#examples)
    - [Reading examples](https://docs.python.org/3.14/library/tarfile.html#reading-examples)
    - [Writing examples](https://docs.python.org/3.14/library/tarfile.html#writing-examples)

  - [Supported tar formats](https://docs.python.org/3.14/library/tarfile.html#supported-tar-formats)
  - [Unicode issues](https://docs.python.org/3.14/library/tarfile.html#unicode-issues)

[Subject index](INDEX.md)
