# gzip - Examples of usage

### Examples of usage

An example showing how to read a compressed file:

```python
import gzip
with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
    file_content = f.read()

```

An example showing how to create a compressed GZIP file:

```python
import gzip
content = b"Lots of content here"
with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
    f.write(content)

```

An example showing how to GZIP compress a file that already exists:

```python
import gzip
import shutil
with open('/home/joe/file.txt', 'rb') as f_in:
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

```

An example showing how to GZIP compress a binary string:

```python
import gzip
s_in = b"Lots of content here"
s_out = gzip.compress(s_in)

```

See also

Module [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib)

The foundational data-compression module required to back the **gzip** file format.

When gzip (de)compression turns into a bottleneck, the [python-isal](https://github.com/pycompression/python-isal) package accelerates (de)compression through a largely compatible API.

[Subject index](INDEX.md) · [Previous](gzip-compress-to-gzip-decompress.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: gzip](gzip-open-to-gzip-badgzipfile.md)
