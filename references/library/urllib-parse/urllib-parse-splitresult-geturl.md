# urllib.parse: `urllib.parse.SplitResult.geturl()`

### Structured Parse Results

The result objects returned by the `urlsplit()`, `urlparse()`, and `urldefrag()` functions are subclasses of the [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) type. These subclasses tack on the attributes listed in those functions’ documentation, the encoding and decoding support covered in the previous section, plus one more method:

 urllib.parse.SplitResult.geturl()

Give back the re-assembled form of the original URL as a string. It may not match the original URL, since the scheme can be normalized to lower case and empty components can be dropped. In particular, empty parameters, queries, and fragment identifiers are removed.

For `urldefrag()` results, only empty fragment identifiers are removed. For `urlsplit()` and `urlparse()` results, every noted change is applied to the URL this method returns.

Feeding this method’s result back through the original parsing function leaves it unchanged:

```python
>>> from urllib.parse import urlsplit
>>> url = 'HTTP://www.Python.org/doc/#'
>>> r1 = urlsplit(url)
>>> r1.geturl()
'http://www.Python.org/doc/'
>>> r2 = urlsplit(r1.geturl())
>>> r2.geturl()
'http://www.Python.org/doc/'

```

These classes supply the implementations of the structured parse results when working on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects:

[Subject index](INDEX.md) · [Previous](parsing-ascii-encoded-bytes.md) · [Continue](urllib-parse-defragresult-class.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md)
