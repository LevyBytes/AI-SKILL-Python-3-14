# wsgiref.util: `wsgiref.util.FileWrapper`

*class *wsgiref.util.FileWrapper(*filelike*, *blksize=8192*)

A concrete realization of the `wsgiref.types.FileWrapper` protocol that turns a file-like object into an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator). The objects produced are [iterable](https://docs.python.org/3.14/glossary.html#term-iterable)s. While the object is being iterated, the optional *blksize* argument gets handed again and again to the *filelike* object’s `read()` method to fetch the bytestrings that are yielded. Once `read()` hands back an empty bytestring, iteration stops and cannot be restarted.

Should *filelike* offer a `close()` method, the object returned will likewise carry a `close()` method, and calling it will trigger the *filelike* object’s `close()` method.

Example usage:

```python
from io import StringIO
from wsgiref.util import FileWrapper

# We're using a StringIO-buffer for as the file-like object
filelike = StringIO("This is an example file-like object"*10)
wrapper = FileWrapper(filelike, blksize=5)

for chunk in wrapper:
    print(chunk)

```

Changed in version 3.11: Support for [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method has been removed.

[Subject index](INDEX.md) · [Previous](wsgiref-util-guess-scheme-to-wsgiref-util-is-hop-by-hop.md) · [Continue](../wsgiref-headers/wsgiref-headers-headers-class.md) · [Owning module, declaration or section: wsgiref.util](wsgiref-util-guess-scheme-to-wsgiref-util-is-hop-by-hop.md)
