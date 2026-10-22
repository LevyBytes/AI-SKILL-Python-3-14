# What's New In Python 3.2 / gzip and zipfile — gzip, io, zipfile

### gzip and zipfile

The [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) is now implemented by [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) (apart from `truncate()`). On top of that it offers a [`peek()`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile.peek) method and copes with both unseekable and zero-padded file objects.

For simpler in-memory compression and decompression, the [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) module also adds the [`compress()`](https://docs.python.org/3.14/library/gzip.html#gzip.compress) and [`decompress()`](https://docs.python.org/3.14/library/gzip.html#gzip.decompress) functions. Remember that text has to be turned into [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) before either compressing or decompressing:

```python
>>> import gzip
>>> s = 'Three shall be the number thou shalt count, '
>>> s += 'and the number of the counting shall be three'
>>> b = s.encode()                        # convert to utf-8
>>> len(b)
89
>>> c = gzip.compress(b)
>>> len(c)
77
>>> gzip.decompress(c).decode()[:42]      # decompress and convert to text
'Three shall be the number thou shalt count'

```

(Work credited to Anand B. Pillai via [bpo-3488](https://bugs.python.org/issue?@action=redirect&bpo=3488); plus Antoine Pitrou, Nir Aides and Brian Curtin via [bpo-9962](https://bugs.python.org/issue?@action=redirect&bpo=9962), [bpo-1675951](https://bugs.python.org/issue?@action=redirect&bpo=1675951), [bpo-7471](https://bugs.python.org/issue?@action=redirect&bpo=7471) and [bpo-2846](https://bugs.python.org/issue?@action=redirect&bpo=2846).)

Furthermore, the internals of the [`zipfile.ZipExtFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.open) class, which stands for files held within an archive, were rebuilt. This new code runs much faster and may be wrapped inside an [`io.BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader) object for extra speed gains. It additionally fixes a bug where mixing *read* and *readline* calls produced incorrect output.

(Patch submitted by Nir Aides in [bpo-7610](https://bugs.python.org/issue?@action=redirect&bpo=7610).)

[Subject index](INDEX.md) · [Previous source section](select.md) · [Next source section](tarfile.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
